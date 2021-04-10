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
def save_links(get_links, u):
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
def save_imgs(get_imgs, u):
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
def save_phone_no(phn):
    try:
        with open("phone_no.txt", "a+") as ph:
            for p in phn:
                ph.write(p + '\n')
    except:
        pass