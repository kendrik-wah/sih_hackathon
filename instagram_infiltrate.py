from bs4 import BeautifulSoup
import json, random, re, requests
from instagram.client import InstagramAPI
from instagram.oauth2 import OAuth2API, OAuth2AuthExchangeRequest
import instagram_private_api
import instagram_web_api
from selenium import webdriver
from urllib.parse import urlparse

user_name = 'gymnopedie_k'
password = 'magnataur'
client_id = '4bf1d80dc15b4d368eb57efe2dd8e367'
client_secret = '1150b494eaa843e58e884a601821fbb4'
access_token = '719197117.4bf1d80.75cc73b79792435f914dee5c2bccd9a5'
scope = ('basic','public_content')

base_url = 'https://www.instagram.com'
accessor_url = base_url + '/' + user_name + '/?__a=1'
login_url = "https://www.instagram.com/accounts/login/"
redirect_uri = 'http://localhost'
acc_tok_url = 'https://www.instagram.com/oauth/authorize/?client_id=' + client_id + '&redirect_uri=' + redirect_uri + '&response_type=token'

authenticated_api = InstagramAPI(access_token=access_token, client_secret=client_secret)
unauthenticated_api = InstagramAPI(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET')

print(authenticated_api)
print(unauthenticated_api)

req = requests.get('https://api.instagram.com/v1/users/self/media/recent/?access_token=' + access_token)
print(req.json())

# driver = webdriver.Chrome(r"C:\Users\kendrik\Documents\Setups\chromedriver_win32\chromedriver.exe")
# driver.get(webdriver)
# username = driver.find_element_by_xpath('//*[@name="username"]')
# password = driver.find_element_by_xpath('//*[@name="password"]')
# login_btn = driver.find_element_by_xpath('//*[@value="Log in"]')
#
# api = InstagramAPI(client_id=client_id, client_secret=client_secret,redirect_uri=redirect_uri)
# redirect_uri = api.get_authorize_login_url(scope=scope)
#
# username.send_keys(user_name)
# password.send_keys(password)
#
# login_btn.click()
# current_url = driver.current_url
# parsed = urlparse(current_url)
# parsed_code = urlparse.parse_qs(parsed.query)['code'][0]
# access_token, user_info = api.exchange_code_for_access_token(parsed_code)
#
# api = InstagramAPI(client_id=client_id,access_token=access_token)
# # helloisden = 512140057
# tag_info = api.tag('nofilter')
# print(tag_info)
#
# #
# # test = requests.get(redirect_uri)
# # print(test.text)
# #
# # req = session.get(accessor_url)


