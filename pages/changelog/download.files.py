import requests

url1 = "https://raw.githubusercontent.com/revanced/revanced-patches/main/CHANGELOG.md"
myfile1 = requests.get(url1, allow_redirects=True)

open("temp/patches.md", "wb").write(myfile1.content)
