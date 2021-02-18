import requests
from pip._vendor.distlib.compat import raw_input


def req(_url):
    try:
        return requests.get("https://" + _url)
    except:
        pass


url = raw_input("Enter the URL:")
file = open("common.txt", "r")
for line in file:
    text = line.strip()
    full_url = url + "/" + text
    res = req(full_url)
    if res:
        print("directory found : " + "https://" + full_url)
file.close()
