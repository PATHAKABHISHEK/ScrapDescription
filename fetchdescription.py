import requests
from bs4 import BeautifulSoup

while True :
    #getting input from user (name of the website)
    url_tag = input("Enter the name of the website that you want to search")

    if(url_tag == "EXIT" or url_tag == "exit"):
        break

    #urltag that we get is in the form of string
    url_string = "http://www." + url_tag + ".com"

    #passing the url_string into the get method of request
    url_page = requests.get(url_string)

    #parsing html document of the site using html parser
    soup = BeautifulSoup(url_page.content, "html.parser")

    #storing title from the parsed html page
    title = soup.find('title').text.strip()

    #storing description from the parsed html page
    webpage_desc = soup.find('meta', attrs = {'name' : 'description'})

    #getting the attribute content from the meta tag
    desc = webpage_desc.attrs['content']

    #printing title, url, description
    print( "\n"+ str(title))
    print(url_string)
    print(desc)

