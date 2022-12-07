import requests

url = "https://raw.githubusercontent.com/revanced/revanced-patches/main/CHANGELOG.md"
myfile = requests.get(url, allow_redirects=True)

open("temp/patches.changelog.md", "wb").write(myfile.content)
