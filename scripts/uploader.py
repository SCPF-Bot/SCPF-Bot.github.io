#!/usr/bin/env python3
"""
Uploader for dl.surf – reads URLs from /hosts/list.txt,
downloads each file into /hosts/temp/, uploads one by one,
then shows success/failure summary.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse

# ------------------------------------------------------------
# Configuration (paths relative to repo root)
# ------------------------------------------------------------
REPO_ROOT = Path(__file__).parent.parent.resolve()   # two levels up from scripts/
LIST_FILE = REPO_ROOT / "hosts" / "list.txt"
TEMP_DIR = REPO_ROOT / "hosts" / "temp"

API_KEY = os.environ.get("DL_SURF_API_KEY")
BASE_URL = "https://api.dl.surf"

# ------------------------------------------------------------
# Validation
# ------------------------------------------------------------
if not API_KEY:
    print("❌ ERROR: Environment variable DL_SURF_API_KEY not set.")
    sys.exit(1)

if not LIST_FILE.is_file():
    print(f"❌ ERROR: List file not found: {LIST_FILE}")
    sys.exit(1)

# Create temp directory (safe, exists_ok=True)
TEMP_DIR.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------
# Helper: upload one file to dl.surf
# ------------------------------------------------------------
def upload_file(file_path: Path):
    """Returns (success: bool, message: str)"""
    try:
        # Step 1: get upload server URL
        resp = requests.get(
            f"{BASE_URL}/api/upload/server",
            params={"key": API_KEY},
            timeout=10
        )
        resp.raise_for_status()

        content_type = resp.headers.get('content-type', '')
        if 'application/json' in content_type:
            data = resp.json()
            upload_url = data.get('url') or data.get('server_url') or data.get('upload_url')
        else:
            upload_url = resp.text.strip()

        if not upload_url:
            return False, "Empty upload URL from API"

        # Step 2: POST file
        with open(file_path, 'rb') as f:
            files = {'file': (file_path.name, f)}
            upload_resp = requests.post(upload_url, files=files, timeout=60)
            upload_resp.raise_for_status()

        return True, "Upload successful"

    except requests.exceptions.Timeout:
        return False, "Timeout during upload"
    except requests.exceptions.RequestException as e:
        return False, f"Request error: {e}"
    except Exception as e:
        return False, f"Unexpected error: {e}"

# ------------------------------------------------------------
# Helper: download a URL to a local file (safe filename)
# ------------------------------------------------------------
def download_file(url: str, dest_dir: Path, index: int) -> (bool, str, Path):
    """Returns (success, message, local_path)"""
    # Create a safe filename from URL basename
    parsed = urlparse(url)
    raw_name = os.path.basename(parsed.path)
    if not raw_name or '.' not in raw_name:
        raw_name = f"downloaded_{index}.bin"
    # Sanitize: remove path separators, keep only safe chars
    safe_name = "".join(c for c in raw_name if c.isalnum() or c in '.-_')
    if not safe_name:
        safe_name = f"file_{index}.dat"

    dest_path = dest_dir / safe_name

    try:
        # Stream download to avoid memory issues
        with requests.get(url, stream=True, timeout=30) as r:
            r.raise_for_status()
            with open(dest_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        return True, "Downloaded", dest_path
    except requests.exceptions.Timeout:
        return False, "Download timeout", dest_path
    except requests.exceptions.RequestException as e:
        return False, f"Download failed: {e}", dest_path
    except Exception as e:
        return False, f"Unexpected download error: {e}", dest_path

# ------------------------------------------------------------
# Main
# ------------------------------------------------------------
def main():
    print(f"📄 Reading URLs from: {LIST_FILE}")
    with open(LIST_FILE, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]

    if not urls:
        print("❌ No URLs found in list.txt")
        sys.exit(1)

    print(f"🚀 Found {len(urls)} URL(s) to process\n")

    results = []   # each: (url, download_ok, upload_ok, message)

    for idx, url in enumerate(urls, start=1):
        print(f"--- [{idx}/{len(urls)}] {url}")

        # Download
        dl_ok, dl_msg, local_path = download_file(url, TEMP_DIR, idx)
        if not dl_ok:
            print(f"   ❌ {dl_msg}")
            results.append((url, False, False, dl_msg))
            continue
        print(f"   ✅ Downloaded -> {local_path.name}")

        # Upload
        up_ok, up_msg = upload_file(local_path)
        print(f"   {'✅' if up_ok else '❌'} Upload: {up_msg}")
        results.append((url, True, up_ok, up_msg))

        # Cleanup local file after upload (save runner disk space)
        try:
            local_path.unlink()
        except OSError:
            pass   # ignore cleanup errors

    # --------------------------------------------------------
    # Summary
    # --------------------------------------------------------
    print("\n" + "=" * 55)
    print("📊 FINAL SUMMARY")
    print("=" * 55)

    total = len(results)
    uploaded_ok = sum(1 for r in results if r[2])   # upload_ok
    download_failed = sum(1 for r in results if not r[1])
    upload_failed = total - uploaded_ok

    print(f"Total URLs processed: {total}")
    print(f"✅ Successfully uploaded: {uploaded_ok}")
    print(f"❌ Upload failures     : {upload_failed}")
    if download_failed > 0:
        print(f"⚠️  Download failures   : {download_failed} (skipped upload)")

    if upload_failed > 0:
        print("\n❌ Failed items:")
        for url, dl_ok, up_ok, msg in results:
            if not up_ok:
                status = "Download failed" if not dl_ok else "Upload failed"
                print(f"   • {url}\n     [{status}] {msg}")

    # Exit with non-zero if any upload failed (useful for CI)
    if upload_failed > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
