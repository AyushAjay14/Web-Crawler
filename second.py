import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
def search_phone_no(ut):
    res = requests.get(ut).text
    numbers = set()
    patt = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
    phones = re.findall(patt, res)
    for i in phones:
        print(i)
        numbers.add(i)
    return (numbers)
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


