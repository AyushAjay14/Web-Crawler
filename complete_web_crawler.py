import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
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
    except:
        pass
    #print(type(soup))
    return soup
def all_links(t):                 # scrapes all the 'a' tags in the soup content
    paras = t.find_all('a')
    get_llinks = set()
    for anchors in paras:
        get_llinks.add((anchors.get('href')))       #scrapes all the links with the 'href' tag
    return(get_llinks)
def save_links(get_links):
    f = open("html.txt", "a+")
    for links in get_links:
        t = re.compile(r'/[a-zA-Z0-9./-_]')
        if(re.match(t, str(links))):
            f.write(u + links + '\n')
        else:
            f.write(str(links) + "\n")
    f.close()
def find_imgs(t):
    get_img = set()
    image = t.find_all('img')
    for img in image:
        get_img.add(img.get('src'))
    return(get_img)
def save_imgs(get_imgs):
    p = open("src.txt", "w+")
    for images in get_imgs:
        t = re.compile(r'/[a-zA-Z0-9./-_]')
        if(re.match(t,images)):
            p.write(u+images + '\n')
        else:
            p.write(images + '\n')
    p.close()
def search_mails(ut):
    req = requests.get(ut).text
    email = re.compile(r"[a-zA-A0-9\.\-+_]+@[a-zA-A0-9\.\-+_]+.[a-zA-A0-9\.\-+_]+.[a-zA-A0-9\.\-+_]+.[a-zA-A0-9\.\-+_]")
    result = re.findall(email, req)
    with open('emails.txt', "w+") as e:
        for i in result:
            #print(i)
            e.write(i + '\n')
def search_phone_no(ut):
    res = requests.get(ut).text
    numbers = set()
    patt = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
    phones = re.findall(patt, res)
    for i in phones:
        #print(i)
        numbers.add(i)
    return (numbers)
def save_phone_no(phn):
    with open("phone_no.txt", "w+") as ph:
        for p in phn:
            ph.write(p + '\n')

def take_ss(url):
    driver = webdriver.Chrome(executable_path='D:\chromedriver_win32\\chromedriver.exe')
    driver.get(url)
    driver.get_screenshot_as_file('wiki.png')
    driver.close()
def find_headers(url):
    resp = requests.get(url)
    heads = resp.headers
    st = str(heads)
    with open("head.txt", 'a+') as n:
        for i in st:
            n.write(i)
        n.write('\n\n')

create_and_change_dir()
u = input("Enter the URL : ")
t = reqs(u)
get_links1 = all_links(t)
save_links(get_links1)
get_img1 = find_imgs(t)
save_imgs(get_img1)
search_mails(u)
t = input('DO you want to take screenshots(y/n) ?')
if(t =="y"):
     take_ss(u)
else:
    pass
nu =search_phone_no(u)
save_phone_no(nu)
find_headers(u)





#print(paras)
