from bs4 import BeautifulSoup
import json, random, re, requests
import pyfacebook
import facebook

graph_uri = 'https://graph.facebook.com'
app_id = '1674160456050056'
app_secret = 'f24802e319591fbfe076f66a314963fa'
access_token = 'EAAXyo9tHpYgBAPqGyTyUZB5TVkOCDZCl6DZA8jXJpKTxQ3ZBzU3JiBFWAe1MkZCMHNM9YAQThfKRRjotjSIaAw7uRshLK6jfDBBFcNDcLhesYjYWa1ZB4hMAOcs4c3uDOXfD76LlSsmn4zaRhW19MR2epi5UyLBLuX5hbto5BjWmjZAmcyXcguf'

graph = facebook.GraphAPI()

app_token = graph.get_app_access_token(app_id, app_secret)
print(app_token)

extended = facebook.GraphAPI(access_token)
print(extended)

extended.extend_access_token(app_id, app_secret)

req = requests.get(graph_uri + '/me' + '&access_token=' + access_token)
print(req.json())

# result = extended.get_object()
# print(result)
