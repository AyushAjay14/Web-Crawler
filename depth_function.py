import phone_no_ss_headers
import links_images_emails
import saving_links_images_phoneno

def open_links(depth, args, argument):
    d = int(0)
    while(d < depth):
        r = open("href_links.txt", 'rt')
        t = r.readlines()
        #print(t)
        queue = set()
        crawled = set()
        for i in t:
            line = i.strip('\n')
            queue.add(line)
        for i in range(len(queue)):
            l = queue.pop()
            if(argument == "y"):
                if("contact" in l):
                    phone_no_ss_headers.take_ss(l)
                elif("admin" in l):
                    phone_no_ss_headers.take_ss(l)
                elif("web-admin" in l):
                    phone_no_ss_headers.take_ss(l)
                elif("backup" in l):
                    phone_no_ss_headers.take_ss(l)
                elif("login" in l):
                    #print("hi")
                    phone_no_ss_headers.take_ss(l)
                else:
                    pass
            #print(l)
            t = links_images_emails.reqs(l)
            #print("==>> Finding links")
            get_links1 = links_images_emails.all_links(t)
            saving_links_images_phoneno.save_links(get_links1, l)
            if(args.imagelinks==1):
                #print("==>> finding imagelinks")
                get_img1 = links_images_emails.find_imgs(t)
                saving_links_images_phoneno.save_imgs(get_img1, l)
            if(args.emails==1):
                #print("==>> finding mails")
                links_images_emails.search_mails(l)
            if(args.phoneno==1):
                #print("==>> finding phoneno")
                nu =phone_no_ss_headers.search_phone_no(l)
                saving_links_images_phoneno.save_phone_no(nu)
            if(args.headers==1):
                #print("==>> finding headers")
                phone_no_ss_headers.find_headers(l)

            crawled.add(l)
        with open("crawled_links.txt", "a+") as crawled_links:
            for p in crawled:
                crawled_links.write(p + "\n")
        d = d + 1
        print("Reached depth : " + str(d))
        r.close()
