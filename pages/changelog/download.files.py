import requests

url-1 = "https://raw.githubusercontent.com/revanced/revanced-patches/main/CHANGELOG.md"
myfile-1 = requests.get(url-1, allow_redirects=True)

open("temp/patches.md", "wb").write(myfile-1.content)
