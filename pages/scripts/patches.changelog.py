import requests

url = "https://raw.githubusercontent.com/revanced/revanced-patches/main/CHANGELOG.md"
myfile = requests.get(url, allow_redirects=True)

open("c:/users/LikeGeeks/documents/hello.pdf", "wb").write(myfile.content)
