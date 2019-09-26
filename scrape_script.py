from instagram_infiltrate import InstagramScrape
from twitter_infiltrate import TwitterTarget
from reddit_scrape import RedditTarget

# need to take relevant values off a person's account
# instagram_handle = InstagramScrape('xxx', 'xxx')
# twitter_handle = TwitterTarget('ChaotiqueEdge')
reddit_handle = RedditTarget()

mental_illnesses = ['depression', 'anxiety', 'stress']

# instagram_handle.scrape(mental_illnesses)
# twitter_handle.scrape(mental_illnesses)
reddit_handle.scrape(mental_illnesses)
