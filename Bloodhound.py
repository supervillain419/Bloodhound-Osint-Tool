from pip._vendor import requests


class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

#ASCII ART
print("""
██████╗ ██╗      ██████╗  ██████╗ ██████╗ ██╗  ██╗ ██████╗ ██╗   ██╗███╗   ██╗██████╗ 
██╔══██╗██║     ██╔═══██╗██╔═══██╗██╔══██╗██║  ██║██╔═══██╗██║   ██║████╗  ██║██╔══██╗
██████╔╝██║     ██║   ██║██║   ██║██║  ██║███████║██║   ██║██║   ██║██╔██╗ ██║██║  ██║
██╔══██╗██║     ██║   ██║██║   ██║██║  ██║██╔══██║██║   ██║██║   ██║██║╚██╗██║██║  ██║
██████╔╝███████╗╚██████╔╝╚██████╔╝██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝
╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝ 
                          OSINT TOOL MADE MY @supervillain419                       """)

#List of Social Medias I will use
social_media = {
    "Facebook" : "https://www.facebook.com/",
    "Instagram" : "https://www.instagram.com/",
    "Github" : "https://github.com/",
    "Chess.com" : "https://chess.com/member/",
    "Vsco" : "https://vsco.co/",
    "Reddit" : "https://www.reddit.com/user/",
    "Flickr" : "https://www.flickr.com/people/",
    "Pinterest" : "https://gr.pinterest.com/",
    "Soundcloud" : "https://soundcloud.com/"
}
# User inserts the name he want to search
usr_input = input("\n> Please enter the name you want to search: ")
print("\n")

backup = ""
#For every Social Media
for sm in social_media:
    url_link = social_media[sm] + usr_input
    # In response variable we get the status code 
    response = requests.get(url_link)
    # Status code: 200 = Exists, 401 = Does not exist!
    if response.status_code == 200:
        print((f"[+] {sm} account") + bcolors.OKGREEN +(" Found! ")+ bcolors.ENDC, end="")
        print(url_link)
        backup += (f"[+] {sm} account Found! ") + url_link + ("\n")
    else:
        print((f"[+] {sm} account") + bcolors.FAIL + (" Not Found! ") + bcolors.ENDC)

save_it = input("\nDo you want to save the results in a text? yes/no: ")
# Option to save the output in a .txt file
if save_it == "yes" or save_it == "y":
    usr_input += ".txt"
    f = open(usr_input, "x")
    f.write(backup)
    f.close()
else:
    print("Thank you for using my tool! :) \n")
