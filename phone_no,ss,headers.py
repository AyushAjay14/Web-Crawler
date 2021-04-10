import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
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
def take_ss(url):
    try:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        #driver = webdriver.Chrome(executable_path='E:\\chromedriver_win32\\chromedriver.exe')
        print("TAKING SCREENSHOT OF: " + url)
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


