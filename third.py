import requests
from bs4 import BeautifulSoup
import re
import second
def save_links(get_links , u):                    # saves all the links in text file
    f = open("html.txt", "a+")
    for links in get_links:
        t = re.compile(r'/[a-zA-Z0-9./-_]')
        if ( re.match(t, links)):
            f.write(u + links + '\n')
        else:
            f.write( links + "\n")
def save_imgs(get_imgs , u):                      #saves all the img links found from the find_imgs function
    p = open("src.txt", "w+")
    for images in get_imgs:
        t = re.compile(r'/[a-zA-Z0-9./-_]')
        if(re.match(t,images)):
            p.write(u+images + '\n')
        else:
            p.write(images + '\n')
    p.close()
def save_phone_no(phn):                            #saves all the phone numbers found in the save_phone_no function
    with open('phone_no.txt', "a+") as ph:
        for p in phn:
            ph.write(p + '\n')