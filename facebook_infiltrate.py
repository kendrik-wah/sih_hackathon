from bs4 import BeautifulSoup
import json, random, re, requests
import pyfacebook
import facebook

app_id = '376395939967416'
app_secret = '52edfbb8fb4f9c59a64613b81b5efc9a'

graph = facebook.GraphAPI()

access_token = graph.get_app_access_token(app_id, app_secret)
print(access_token)