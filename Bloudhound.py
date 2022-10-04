from pip._vendor import requests


#List of Social Medias I will use
social_media = {
    "Facebook" : "https://www.facebook.com/",
    "Instagram" : "https://www.instagram.com/",
    "Github" : "https://github.com/",
    "Chess.com" : "https://chess.com/member/",
    "Vsco" : "https://vsco.co/",
    "Reddit" : "https://www.reddit.com/user/",
    "Flickr" : "https://www.flickr.com/people",
    "Pinterest" : "https://gr.pinterest.com/",
    "Soundcloud" : "https://soundcloud.com/"
}
# User inserts the name he want to search
usr_input = input("> Please enter the name you want to search:")

#For every Social Media
for sm in social_media:
    url_link = social_media[sm] + usr_input
    # In response variable we get the status code 
    response = requests.get(url_link)
    # Status code: 200 = Exists, 401 = Does not exist!
    if response.status_code == 200:
        print(f"The user has an {sm} account!")
        print(url_link,"\n")
    else:
        print(f"{sm}: Not Found!")