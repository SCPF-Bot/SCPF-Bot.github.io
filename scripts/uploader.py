import requests
import os

# --- Configuration ---
API_KEY = os.environ.get("DL_SURF_API_KEY")
LIST_FILE = "/hosts/list.txt"
TEMP_DIR = "/hosts/temp/"

def get_upload_server(api_key):
    """
    Step 1: The Handshake.
    Requests the current active upload server from the gateway.
    """
    gateways = [
        "https://dl.surf/api/upload/server",
        "https://api.dl.surf/api/upload/server"
    ]
    
    for gw in gateways:
        try:
            # We use a GET request to ask for the server
            resp = requests.get(gw, params={'key': api_key}, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                # Most PPD APIs return the server URL in 'result' or 'url'
                server_url = data.get('result') or data.get('url')
                if server_url:
                    return server_url
        except:
            continue
    return None

def download_file(url):
    """Downloads a file from a URL to the temp directory."""
    try:
        local_filename = os.path.join(TEMP_DIR, url.split('/')[-1].split('?')[0])
        print(f"📥 Downloading: {url.split('/')[-1]}...")
        with requests.get(url, stream=True, timeout=60) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        return local_filename
    except Exception as e:
        print(f"❌ Download Error: {e}")
        return None

def upload_to_server(file_path, server_url, api_key):
    """
    Step 2: The Upload.
    Sends the local file to the server discovered in Step 1.
    """
    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            payload = {'key': api_key, 'action': 'upload'}
            
            # Use a longer timeout for the actual file transfer
            response = requests.post(server_url, params=payload, files=files, timeout=600)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 200 or data.get('success'):
                    return True, data.get('url')
                else:
                    return False, data.get('msg', 'API rejected upload')
            return False, f"HTTP {response.status_code}"
    except Exception as e:
        return False, str(e)

def main():
    if not API_KEY:
        print("❌ CRITICAL: DL_SURF_API_KEY environment variable is missing.")
        return

    # 1. Setup Environment
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

    if not os.path.exists(LIST_FILE):
        print(f"❌ CRITICAL: {LIST_FILE} not found.")
        return

    # 2. Read URLs
    with open(LIST_FILE, "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    print(f"🚀 Starting Pipeline: {len(urls)} files in queue.")
    print("-" * 50)

    for url in urls:
        # Step A: Download
        local_file = download_file(url)
        if not local_file:
            continue

        # Step B: Get Upload Server (Handshake)
        server = get_upload_server(API_KEY)
        if not server:
            print("⚠️ Could not find dynamic server. Falling back to static...")
            server = "https://dl.surf/api/file/upload"

        # Step C: Upload
        print(f"📤 Uploading to: {server}...")
        success, result = upload_to_server(local_file, server, API_KEY)

        # 3. Indicators & Cleanup
        if success:
            print(f"✅ SUCCESS: {result}")
            os.remove(local_file) # Delete after success to save space
        else:
            print(f"❌ FAILED: {result}")
            # We keep the file in /temp/ if it fails so you can check it
        
        print("-" * 50)

if __name__ == "__main__":
    main()
