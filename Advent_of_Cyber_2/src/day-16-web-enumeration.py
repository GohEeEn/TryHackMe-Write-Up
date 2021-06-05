#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests


def task2(url):

    # Download the webpage and stores it as a variable
    # Reference : https://stackoverflow.com/questions/36709165/beautifulsoup-object-of-type-response-has-no-len
    html = requests.get(url).text

    # Parse the webpage into something that beautifulsoup can read over
    # lxml is the parser for reading the html
    soup = BeautifulSoup(html, "html.parser")

    # Reference : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    for link in soup.find_all('a'):
        print(link.get('href'))


def task3(url):

    found = False

    # Task 3
    for api_key in range(1, 100, 2):
        json = requests.get(f'{url}/api/{api_key}').json()
        if((json['q'] != "Error. Key not valid!") and (json['q'] != "SANTA PROTECTION MECHANISM ACTIVATED.")):
            print(f"api_key = {api_key}, {json['q']}")
            found = True
            break
    if(not found):
        print('Target not found. Restart VM may required')


### Start scripting ###
domain = "10.10.185.174"
port = ""
url = 'http://' + domain + ':' + port

task3(url)
