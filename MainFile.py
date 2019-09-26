from urllib.request import urlopen
from urllib.parse import urlencode
import json
import requests
import facebook
from bs4 import BeautifulSoup
from selenium import webdriver

# access_token='719197117.4bf1d80.c7af0e7fa9a6492283c8ca52ed8393cf'
# client_id='4bf1d80dc15b4d368eb57efe2dd8e367'
# client_secret='1150b494eaa843e58e884a601821fbb4'

import numpy
import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
from sklearn.model_selection import train_test_split # function for splitting data to train and test sets

from nltk import tokenize
from nltk.classify import NaiveBayesClassifier
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
from nltk.corpus import stopwords
from nltk.classify import SklearnClassifier
sid = SentimentIntensityAnalyzer()

test_sentence = 'I love Fortnite so much! It is the best game ever!'
tricky_sentence = 'Sentiment analysis has never been good.'
paragraph = "It was one of the worst movies I've seen, despite good reviews.\nUnbelievably bad acting!! Poor direction. VERY poor production. \nThe movie was bad. Very bad movie. VERY bad movie. VERY BAD movie. VERY BAD movie!"
new_sentence = "The plot was good, but the characters are uncompelling and the dialog is not great."

lines_list = []
test_sentences = [tricky_sentence]
test_test = tokenize.sent_tokenize(test_sentence)
lines_list = tokenize.sent_tokenize(paragraph)
test_sentences.extend(test_test)
test_sentences.extend(lines_list)
test_sentences.append(new_sentence)

tldr = {'positive': 0,
        'neutral': 0,
        'negative': 0}

for sentence in test_sentences:
    ss = sid.polarity_scores(sentence)
    print(sentence, ':', ss['compound'])
    if ss['compound'] == 0.0:
        tldr['neutral'] += 1
    elif ss['compound'] > 0.0:
        tldr['positive'] += 1
    else:
        tldr['negative'] += 1

print(tldr)

