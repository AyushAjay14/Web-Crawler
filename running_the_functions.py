import saving_links_images_phoneno
import links_images_emails
import argparse
from colorama import Fore
import phone_no_ss_headers
import depth_function
saving_links_images_phoneno.create_and_change_dir()
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
t = links_images_emails.reqs(u)
get_links1 = links_images_emails.all_links(t)
saving_links_images_phoneno.save_links(get_links1, u)
if(args.imagelinks==1):
    get_img1 = links_images_emails.find_imgs(t)
    saving_links_images_phoneno.save_imgs(get_img1, u)
if(args.emails==1):
    links_images_emails.search_mails(u)
argument = input(Fore.RED + 'DO you want to take screenshots(y/n) ?')
if(argument =="y" ):
    if("contact" in str(u)):
        phone_no_ss_headers.take_ss(u)
    elif("admin" in u):
        phone_no_ss_headers.take_ss(u)
    elif("web-admin" in u):
        phone_no_ss_headers.take_ss(u)
    elif("backup" in u):
        phone_no_ss_headers.take_ss(u)
    elif("login" in u):
        phone_no_ss_headers.take_ss(u)
    else:
        pass
print(Fore.RED + '==>>', Fore.CYAN + 'web crawling has succesfully started' )
if(args.phoneno==1):
    nu =phone_no_ss_headers.search_phone_no(u)
    saving_links_images_phoneno.save_phone_no(nu)
if(args.headers==1):
    phone_no_ss_headers.find_headers(u)
if(dep==1):
    print(Fore.RED + '==>>' + Fore.CYAN + "web crawing is completed")
else:
    depth_function.open_links(dep, args, argument)
    print(Fore.RED + '==>>' + Fore.CYAN + "web crawing is completed")



#print(paras)
