#!/usr/bin/python3

import requests

host = 'http://10.10.169.100:3000/'
flag = 's'
path = 'f'

while(True):
    response = requests.get(host + path)
    json_response = response.json()
    if(json_response['value'] != 'end'):
        flag += json_response['value']
        path = json_response['next']
    else:
        break

print("Flag : " + flag)
