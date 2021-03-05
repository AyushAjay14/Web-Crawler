import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver

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
def save_links(get_links):          # saves all the links in text file
    f = open("html.txt", "a+")
    for links in get_links:
        t = re.compile(r'/[a-zA-Z0-9./-_]')                    
        if ( re.match(t, links)):                       #it checks if the link starts with a '/' then 
            f.write(u + links + '\n')                   # adds the url inputted by the user,at the beginning of the link
        else:
            f.write( links + "\n")
    f.close()
def find_imgs(t):                           #scrapes all the image links from the website
    get_img = set()
    image = t.find_all('img')               #finds all the img tags from the beautifulsoup object
    for img in image:
        get_img.add(img.get('src'))
    return(get_img)
def save_imgs(get_imgs):                    #saves all the img links found from the find_imgs function
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
def search_phone_no(ut):                 #scrapes all the phone numbers 
    res = requests.get(ut).text
    numbers = set()
    patt = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
    phones = re.findall(patt, res)
    for i in phones:
        print(i)
        numbers.add(i)
    return (numbers)
def save_phone_no(phn):                   #saves all the phone numbers found in the save_phone_no function
    with open("phone_no.txt", "a+") as ph:
        for p in phn:
            ph.write(p + '\n')

def take_ss(url):                         #function to take the screenshot 
    driver = webdriver.Chrome(executable_path='D:\chromedriver_win32\\chromedriver.exe')
    driver.get(url)
    driver.get_screenshot_as_file('wiki.png')
    driver.close()
def find_headers(url):                     #scrapes all the http headers
    resp = requests.get(url)
    heads = resp.headers
    st = str(heads)
    with open("head.txt", 'a+') as n:
        for i in st:
            n.write(i)
        n.write('\n\n')


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
search_phone_no(u)
find_headers(u)





#print(paras)
