import requests
import os
import webbrowser
import time
import re
import json
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

consumer_key = os.environ['POCKET_SECRET']

# URLs
request_url = 'https://getpocket.com/v3/oauth/request'
auth_base_url = 'https://getpocket.com/auth/authorize'
access_url = 'https://getpocket.com/v3/oauth/authorize'
get_url = 'https://getpocket.com/v3/get'
redirect_uri = 'http://daveaseeman.github.io'


# Get Request Token
print('getting request token')
request_token = requests.post(request_url,
                              data={'consumer_key': consumer_key,
                                    'redirect_uri': redirect_uri}
                              )
request_token = request_token.text.replace('code=', '')
rt_len = len(request_token)
if rt_len == 30:
    print('request token received')
else:
    print('problem with request token')

# User Authorization
token_param = '?request_token=' + request_token
redirect_param = '&redirect_uri=' + redirect_uri
redirect_url = auth_base_url + token_param + redirect_param
print('opening redirect url for authentication')
webbrowser.open(redirect_url, new=2)
time.sleep(5)

# Get Access Token
print('getting access token')
access_token = requests.post(access_url,
                             data={'consumer_key': consumer_key,
                                   'code': request_token}
                             )
contents = re.split(r'[=&]', access_token.text)
access_token = contents[1]
user_name = contents[3]
at_len = len(access_token)
if at_len == 30:
    print('access token is received')
else:
    print('problem with access token')


# Get List
def get_list(count, tag):
    pocket_list = requests.post(get_url,
                                data={'consumer_key': consumer_key,
                                      'access_token': access_token,
                                      'count': count,
                                      'tag': tag}
                                )
    parsed = json.loads(pocket_list.text)
    parsed_list = parsed['list']
    title_list = "Titles:"
    for item in parsed_list:
        title = parsed_list[item]['resolved_title'].encode('utf-8')
        title_list += "\n" + title
    return title_list


count = "10"
tag = "design"
print(get_list(count, tag))
