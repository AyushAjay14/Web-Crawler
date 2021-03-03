import requests
from bs4 import BeautifulSoup
import re
def reqs(url):                   #takes the url and gets the response from the server and creates the beautifulsoup object
    resp = requests.get(url).text
    soup = BeautifulSoup(resp, "lxml")
    #print(type(soup))
    return soup
def all_links(t):                 # scrapes all the 'a' tags in the soup content
    paras = t.find_all('a')
    get_llinks = set()
    for anchors in paras:
        get_llinks.add((anchors.get('href')))       #scrapes all the links with the 'href' tag
    return(get_llinks)
def find_imgs(t):
    get_img = set()
    image = t.find_all('img')
    for img in image:
        get_img.add(img.get('src'))
    return(get_img)
def search_mails(ut):
    req = requests.get(ut).text
    email = re.compile(r"[a-zA-A0-9\.\-+_]+@[a-zA-A0-9\.\-+_]+.[a-zA-A0-9\.\-+_]+.[a-zA-A0-9\.\-+_]+.[a-zA-A0-9\.\-+_]")
    result = re.findall(email, req)
    with open('emails.txt', "w+") as e:
        for i in result:
            print(i)
            e.write(i + '\n')
