import re
from os.path import join
import urllib.request

from instagram_infiltrate import InstagramScrape
from twitter_infiltrate import TwitterTarget
from reddit_scrape import RedditTarget
import json

import nltk

from nltk import tokenize
from nltk.classify import NaiveBayesClassifier
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
from nltk.corpus import stopwords
from nltk.classify import SklearnClassifier

sid = SentimentIntensityAnalyzer()

try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
path = r"C:\Users\kendrik\Pictures\sih_instagram\\"

def read_json_file(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data

def get_instagram_json(file):
    data = read_json_file(file)
    return data


def get_twitter_json(file):
    data = read_json_file(file)
    return data


def get_reddit_json(file):
    data = read_json_file(file)
    return data

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ", tweet).split())

class Account(object):
    def __init__(self):
        self.instagram_username = ''
        self.instagram_password = ''
        self.instagram_account = None
        self.twitter_username = ''
        self.twitter_account = None
        self.instagram_filename = ''
        self.twitter_filename = ''
        self.extracted_instagram_count = 0
        self.extracted_twitter_count = 0

    def log_into_instagram(self, username, password):
        self.instagram_username = username
        self.instagram_password = password
        self.instagram_account = InstagramScrape(self.instagram_username, self.instagram_password)

    def log_into_twitter(self, username):
        self.twitter_username = username
        self.twitter_account = TwitterTarget(self.twitter_username)

    def extract_from_instagram(self):
        instagram_results = self.instagram_account.scrape_self()
        self.instagram_filename = 'instagram_' + self.instagram_username + '.json'

    def extract_from_instagram_offline(self):
        self.instagram_account.save_self_scraped_information()

    def extract_from_twitter(self):
        twitter_results = self.twitter_account.scrape_self()
        self.twitter_filename = 'twitter_' + self.twitter_username + '.json'

    def extract_from_twitter_offline(self):
        self.twitter_account.save_self_scraped_information()

    def analyze_instagram_feed(self, filename):
        extracted_json = get_instagram_json(filename)
        summary_text = {'negative': 0, 'positive': 0, 'neutral': 0}
        summary_media = {'negative': 0, 'positive': 0, 'neutral': 0}
        existing_text = []
        existing_media = []

        for post in extracted_json:
            text = post['text']
            media = post['url']
            tokenized_text = tokenize.sent_tokenize(text)

            for txt in tokenized_text:
                print('text: ', txt)
                if txt not in existing_text:
                    if txt is not None:
                        ss = sid.polarity_scores(txt)
                        print('results: ', ss)
                        if ss['compound'] < 0:
                            summary_text['negative'] = summary_text['negative'] + 1
                        elif ss['compound'] == 0:
                            summary_text['neutral'] = summary_text['neutral'] + 1
                        else:
                            summary_text['positive'] = summary_text['positive'] + 1

                        existing_text.append(txt)

            if media not in existing_media:
                if media is not None:
                    online_url = media.split("/")[6].split("?")
                    img_url = online_url[0]
                    save_path = path + img_url
                    urllib.request.urlretrieve(online_url, save_path)
                    img = Image.open(save_path)
                    attempt_text = pytesseract.image_to_string(img)

                    if len(attempt_text) > 0:
                        ss = sid.polarity_scores(attempt_text)
                        print('results: ', ss)
                        if ss['compound'] < 0:
                            summary_text['negative'] = summary_text['negative'] + 1
                        elif ss['compound'] == 0:
                            summary_text['neutral'] = summary_text['neutral'] + 1
                        else:
                            summary_text['positive'] = summary_text['positive'] + 1

                        existing_text.append(attempt_text)


                    existing_media.append(media)

        return summary_text

    def analyze_twitter_feed(self, filename):
        extracted_json = get_twitter_json(filename)
        summary_text = {'negative': 0, 'positive': 0, 'neutral': 0}
        summary_media = {'negative': 0, 'positive': 0, 'neutral': 0}
        existing_text = []
        existing_media = []

        for post in extracted_json:
            text = post['text']
            media = post['media']

            if text not in existing_text:
                if text is not None:
                    text = clean_tweet(text)
                    ss = sid.polarity_scores(text)
                    print(text)
                    print(ss)
                    if ss['compound'] < 0:
                        summary_text['negative'] = summary_text['negative'] + 1
                    elif ss['compound'] == 0:
                        summary_text['neutral'] = summary_text['neutral'] + 1
                    else:
                        summary_text['positive'] = summary_text['positive'] + 1

                    existing_text.append(text)

            if media not in existing_media:
                if media is not None:
                    online_url = media.split("/")[4]
                    img_url = online_url[0]
                    save_path = path + img_url
                    urllib.request.urlretrieve(online_url, save_path)
                    img = Image.open(save_path)
                    attempt_text = pytesseract.image_to_string(img)
                    if attempt_text != '' or attempt_text is not None:
                        ss = sid.polarity_scores(attempt_text)
                        print('results: ', ss)
                        if ss['compound'] < 0:
                            summary_text['negative'] = summary_text['negative'] + 1
                        elif ss['compound'] == 0:
                            summary_text['neutral'] = summary_text['neutral'] + 1
                        else:
                            summary_text['positive'] = summary_text['positive'] + 1

                        existing_text.append(attempt_text)

                    existing_media.append(media)

        return summary_text


acc = Account()
# acc.log_into_instagram("xxxxxxxxxx", "xxxxxxxxxxx")
# acc.extract_from_instagram_offline()
# extracted_instagram = acc.analyze_instagram_feed('insert json file here')
# acc.log_into_twitter("depressingmsgs")
# acc.extract_from_twitter_offline()
# extracted_twitter = acc.analyze_twitter_feed('insert json file here')

# print(extracted_instagram)
# print(extracted_twitter)
#
#    Pipeline will work like this:
# 1) Get credentials of users (username and password for Instagram, username for Twitter)
# 2) Upon login, can immediately do extract_from_instagram() and extract_from_twitter()
# 3) After doing extraction, use analyze_instagram_feed() and analyze_twitter_feed() (use offline methods if you wish to extract via json instead)
#    These analyze methods will have the NLP and image-to-string codes inside.