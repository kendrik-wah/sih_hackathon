from bs4 import BeautifulSoup
import json, random, re, requests
import twitter

consumer_API_key = "8mo1oe5PCYxRzXytj8lK9beaM"
consumer_secret_API_key = "E7l6T7MYBCn05YGLA05tfVz9NKIfBNKJR79JjxALntnr6je113"
access_token = "805220750042857472-n3zPdbfnjMLn1QpWV7igz42vG7Eqrvz"
secret_access_token = "c19vA2yQQ0a0gYhMpcKzAehi6vKgJLUSZMFzVuYjEOchT"

api = twitter.Api(consumer_key=consumer_API_key,
                  consumer_secret=consumer_secret_API_key,
                  access_token_key=access_token,
                  access_token_secret=secret_access_token)

search_user_result = api.GetUserTimeline(screen_name="BeyondBrokenDep",
                                         count=200)



print(search_user_result)