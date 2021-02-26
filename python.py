import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver

def reqs(url):                   #takes the url and gets the response from the server and creates the beautifulsoup object
    resp = requests.get(url).text
    soup = BeautifulSoup(resp, "lxml")
    #print(type(soup))
    return soup
def all_links(t):          # scrapes all the a tags in the soup content
    paras = t.find_all('a')
    get_llinks = set()
    for anchors in paras:
        get_llinks.add((anchors.get('href')))          #scrapes all the links with the 'href' tag
    return(get_llinks)
def save_links(get_links):
    f = open("html.txt", "a+")
    for links in get_links:
        t = re.compile(r'/[a-zA-Z0-9./-_]')
        if ( re.match(t, links)):
            f.write(u + links + '\n')
        else:
            f.write( links + "\n")
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
            print(i)
            e.write(i + '\n')

def take_ss(url):
    driver = webdriver.Chrome(executable_path='D:\chromedriver_win32\\chromedriver.exe')
    driver.get(url)
    driver.get_screenshot_as_file('wiki.png')
    driver.close()


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






#print(paras)
