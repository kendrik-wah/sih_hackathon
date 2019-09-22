from urllib.request import urlopen
from urllib.parse import urlencode
import json
import requests
import facebook
from bs4 import BeautifulSoup
from selenium import webdriver

app_id = '376395939967416'
app_secret = '52edfbb8fb4f9c59a64613b81b5efc9a'
access_token = 'EAAXyo9tHpYgBAJxwRa4rCFo0gVeKhgZA1rqyWAQr2ww4gi0ORYOHxhkZBIRmn2tEXVXKHvDPxVsnpZCxMtZCdQpQtnMuJpDQMeIWKJ9hbgVffhlh0sCAqHrxOGpT4M30ManQGFTJP05ALE6OquQiiPEBSMZCWdxYxalBlGfieE4f3JbZBnQTnU'
redirect_uri = 'http://www.localhost'
graph_uri = 'https://graph.facebook.com'
login_uri = 'https://www.facebook.com/login/'
facebook_uri = 'https://www.facebook.com/'
user_name = 'sean.kagamine'

username = 'k3ndrik_wah@yahoo.com.sg'
password = 'xxxxxxxxx'

# req = requests.get(graph_uri + '/me' + '&access_token=' + access_token)
# identity_no = req.json()
# print(req.json())

req = requests.Session()
test = req.get(facebook_uri + user_name)
print(test.text)

# req2 = requests.get(graph_uri + '/' + identity_no + '?fields=feed&access_token=' + access_token)
# print(req2.json())

##################################################################################################################

# req = requests.get('https://www.facebook.com/sean.kagamine')
# txt = req.text
# doc = BeautifulSoup(txt, 'html.parser')
# print(doc.prettify)

# graph = facebook.GraphAPI(access_token)

###################################################################################################################

# Get User Token
# def get_user_token(
#     username,
#     password
# ):
#     browser = webdriver.Chrome(r'C:\Program Files\JetBrains\PyCharm Community Edition 2019.2.2\bin\chromedriver.exe')
#     GraphAPIExplorer = 'https://developers.facebook.com/tools/explorer'
#     browser.get(GraphAPIExplorer)
#     login = browser.find_element_by_link_text('Log In')
#     login.click()
#     email = browser.find_element_by_name('email')
#     email.send_keys(username)
#     pwrd = browser.find_element_by_name('pass')
#     pwrd.send_keys(password)
#     login = browser.find_element_by_name('login')
#     login.click()
#     page = BeautifulSoup(browser.page_source,'lxml')
#     browser.quit()
#     token_element = [item for item in page.select('input[type="text"]')
#         if 'placeholder' in item.attrs
#         and 'Access Token' in item['placeholder']]
#     token = token_element[0]['value']
#     return token
#
# token = get_user_token('k3ndrik_wah@yahoo.com.sg', 'Gymnopedie123!')
#
# print(token)

###################################################################################################################

