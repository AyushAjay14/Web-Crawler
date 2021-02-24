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
def save_links(get_links):
    f = open("html.txt", "a+")
    for links in get_links:
        t = re.match(r"^/", links)
        if (t == 'TRUE'):
            f.write(u + links)
        else:
            f.write(u + links + "\n")
    f.close()
def find_imgs(t):
    get_img = set()
    image = t.find_all('img')
    for img in image:
        get_img.add(u + img.get('src'))
    return(get_img)
def save_imgs(get_imgs):
    p = open("src.txt", "w+")
    for images in get_imgs:
        p.write(images + '\n')
    p.close()

u = input("Enter the URL : ")
t = reqs(u)
get_links1 = all_links(t)
save_links(get_links1)
get_img1 = find_imgs(t)
save_imgs(get_img1)




#print(paras)
