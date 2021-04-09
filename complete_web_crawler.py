import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import os
import shutil
import argparse
import random
from webdriver_manager.chrome import ChromeDriverManager
from colorama import Fore, Back, Style
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
def save_links(get_links):
    try:
        f = open("href_links.txt", "w+")
        for links in get_links:
            t = re.compile(r'/[a-zA-Z0-9./-_]')
            if(re.match(t, str(links))):
                f.write(u + links + '\n')
            else:
                f.write(str(links) + "\n")
        f.close()
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
def save_imgs(get_imgs):
    try:
        p = open("image_src_links.txt", "a+")
        for images in get_imgs:
            t = re.compile(r'/[a-zA-Z0-9./-_]')
            if(re.match(t,images)):
                p.write(u+images + '\n')
            else:
                p.write(images + '\n')
        p.close()
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
def search_phone_no(ut):
    try:
        res = requests.get(ut).text
        numbers = set()
        patt = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
        phones = re.findall(patt, res)
        for i in phones:
            #print(i)
            numbers.add(i)
        return (numbers)
    except:
        pass
def save_phone_no(phn):
    try:
        with open("phone_no.txt", "a+") as ph:
            for p in phn:
                ph.write(p + '\n')
    except:
        pass

def take_ss(url):
    try:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        #driver = webdriver.Chrome(executable_path='E:\\chromedriver_win32\\chromedriver.exe')
        browser.get(url)
        browser.get_screenshot_as_file('screenshot' + str(random.randint(1,1000)) + '.png')
        browser.close()
    except:
        pass
def find_headers(url):
    try:
        resp = requests.get(url)
        heads = resp.headers
        st = str(heads)
        with open("http_headers.txt", 'a+') as n:
            for i in st:
                n.write(i)
            n.write('\n\n')
    except:
        pass
def open_links(depth, args):
    d = int(0)
    while(d < depth):
        r = open("href_links.txt", 'rt')
        t = r.readlines()
        #print(t)
        queue = []
        crawled = set()
        for i in t:
            line = i.strip('\n')
            queue.append(line)
        for i in range(len(queue)):
            l = queue.pop(0)
            #print(l)
            t = reqs(l)
            #print("==>> Finding links")
            get_links1 = all_links(t)
            save_links(get_links1)
            if(args.imagelinks==1):
                #print("==>> finding imagelinks")
                get_img1 = find_imgs(t)
                save_imgs(get_img1)
            if(args.emails==1):
                #print("==>> finding mails")
                search_mails(l)
            if(args.phoneno==1):
                #print("==>> finding phoneno")
                nu =search_phone_no(l)
                save_phone_no(nu)
            if(args.headers==1):
                #print("==>> finding headers")
                find_headers(l)
            if("contact" in str(u)):
                take_ss(u)
            elif("admin" in u):
                take_ss(u)
            elif("web-admin" in u):
                take_ss(u)
            elif("backup" in u):
                take_ss(u)
            elif("login" in u):
                take_ss(u)
            else:
                pass
            crawled.add(l)
        with open("crawled_links.txt", "a+") as crawled_links:
            for p in crawled:
                crawled_links.write(p + "\n")
        d = d + 1
        print("Reached depth : " + str(d))
        r.close()
create_and_change_dir()
parser = argparse.ArgumentParser()
parser.add_argument("--url", help="add the url ")
parser.add_argument("--depth",type= int,  help="add the depth which you want to specify")
parser.add_argument("--headers",default= 1,  help="to extract all the headers from the website")
parser.add_argument("--phoneno",default= 1,  help="to extract all the phone numbers")
parser.add_argument("--imagelinks",default= 1,  help="to extract all the image links from the website")
parser.add_argument("--emails",default= 1,  help="to extract all the emails from the website")
args = parser.parse_args()
u = args.url
dep = args.depth
t = reqs(u)
get_links1 = all_links(t)
save_links(get_links1)
if(args.imagelinks==1):
    get_img1 = find_imgs(t)
    save_imgs(get_img1)
if(args.emails==1):
    search_mails(u)
t = input(Fore.MAGENTA + 'DO you want to take screenshots(y/n) ?')
if(t =="y" ):
    if("contact" in str(u)):
        take_ss(u)
    elif("admin" in u):
        take_ss(u)
    elif("web-admin" in u):
        take_ss(u)
    elif("backup" in u):
        take_ss(u)
    elif("login" in u):
        take_ss(u)
    else:
        pass
print(Fore.RED + '==>>', Fore.CYAN + 'web crawling has succesfully started' )
if(args.phoneno==1):
    nu =search_phone_no(u)
    save_phone_no(nu)
if(args.headers==1):
    find_headers(u)
if(dep==1):
    print("web crawing is completed")
else:
    open_links(dep, args)
    print("web crawing is completed")



#print(paras)
