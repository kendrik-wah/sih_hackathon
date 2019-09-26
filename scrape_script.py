import pickle

import instagram_infiltrate
import twitter_infiltrate
import reddit_scrape

mental_illnesses = ['depression', 'anxiety', 'stress']

# need to take relevant values off a person's account
instagram_handle = instagram_infiltrate.InstagramScrape('xxxxxxx', 'xxxxxxx')
twitter_handle = twitter_infiltrate.TwitterTarget('ChaotiqueEdge')
reddit_handle = reddit_scrape.RedditTarget()

# instagram_handle.scrape(mental_illnesses)
# twitter_handle.scrape(mental_illnesses)
reddit_handle.scrape(mental_illnesses)
    
# loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
#
# result_ig = loaded_model.predict(instagram_list_data)
# result_rd = loaded_model.predict(reddit_list_data)
# result_tw = loaded_model.predict(twitter_list_data)
#
#
# print(result_ig)
# print(result_rd)
# print(result_tw)
