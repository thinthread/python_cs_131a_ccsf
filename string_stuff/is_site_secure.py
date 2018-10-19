def is_secure_site(url):
    """ Given a URL, check whether this URL belongs to a secure site, eg:'https:'"""
    
    if url[0:6] == "https:":
        return "YAY,this site is secure!"
    else:
        return "Sorry, this is not a secure site... :-(("

def main():
    
    url_to_check = input("Please submit a url to check if it secure: ")
    print(is_secure_site(url_to_check))

main()