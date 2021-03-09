import first
import second
import third

u = input("Enter the URL : ")
t = first.reqs(u)
get_links1 = first.all_links(t)
third.save_links(get_links1 , u)
get_img1 = first.find_imgs(t)
third.save_imgs(get_img1, u)
first.search_mails(u)
t = input('DO you want to take screenshots(y/n) ?')
if(t =="y"):
     second.take_ss(u)
else:
    pass
no = second.search_phone_no(u)
third.save_phone_no(no)
second.find_headers(u)

