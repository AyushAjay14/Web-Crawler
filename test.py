import requests
from bs4 import BeautifulSoup
import re


def reqs(url):
    resp = requests.get(url).text
    soup = BeautifulSoup(resp, "lxml")
    print(type(soup))
    return soup
def all_links(t):
    paras = t.find_all('a')
    get_llinks = set()
    for anchors in paras:
        get_llinks.add((anchors.get('href')))
    return(get_llinks)
u = input("Enter the URL : ")   
t = reqs(u)
get_links = all_links(t)
f = open("html.txt", "a+")
for links in get_links:
    if (t == 'TRUE'):
        t = re.match(r"^/", links)
        print(t)
        f.write(u + links)
    else:
        f.write(u + links + "\n")


#print(paras)
