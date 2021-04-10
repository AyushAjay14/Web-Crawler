import requests
from bs4 import BeautifulSoup
import re
import os
import shutil
def create_and_change_dir():
    dir = os.getcwd()
    path = os.path.join(dir,'crawleroutput')
    if(os.path.exists(path)):
        shutil.rmtree(path)
        os.makedirs(path)
        os.chdir(path)
    else:
        os.makedirs(path)
        os.chdir(path)
def reqs(url):
    headers_dict = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1"}  #takes the url and gets the response from the server and creates the beautifulsoup object
    try:
        resp = requests.get(url, headers = headers_dict).text
        soup = BeautifulSoup(resp, "lxml")
        return soup
    except:
        pass
    #print(type(soup))
def all_links(t):                 # scrapes all the 'a' tags in the soup content
    try:
        paras = t.find_all('a')
        get_llinks = set()
        for anchors in paras:
            get_llinks.add((anchors.get('href')))       #scrapes all the links with the 'href' tag
        return(get_llinks)
    except:
        pass
def find_imgs(t):
    try:
        get_img = set()
        image = t.find_all('img')
        for img in image:
            get_img.add(img.get('src'))
        return(get_img)
    except:
        pass
def search_mails(ut):
    try:
        req = requests.get(ut).text
        email = re.compile(r"[a-zA-A0-9\.\-+_]+@[a-zA-A0-9\.\-+_]+.[a-zA-A0-9\.\-+_]+.[a-zA-A0-9\.\-+_]+.[a-zA-A0-9\.\-+_]")
        result = re.findall(email, req)
        with open('emails.txt', "a+") as e:
            for i in result:
                #print(i)
                e.write(i + '\n')
    except:
        pass
