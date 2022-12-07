import requests

url_1 = "https://raw.githubusercontent.com/revanced/revanced-patches/main/CHANGELOG.md"
myfile_1 = requests.get(url_1, allow_redirects=True)

open("temp/patches.md", "wb").write(myfile_1.content)
