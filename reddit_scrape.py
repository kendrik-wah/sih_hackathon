import praw

class RedditTarget(object):

    def __init__(self):
        self.client_id = 'nOU50agIaLiB_A'
        self.secret = 'VSW6KfIBnCyh2nJ0eMyLE52mY6s'
        self.user_agent = 'sih_test'
        self.reddit = praw.Reddit(client_id=self.client_id,
                                  client_secret=self.secret,
                                  user_agent=self.user_agent)

    def search_subreddit(self, term, params='all'):
        if params == 'all':
            return self.reddit.subreddit(term).top(params)
        else:
            return self.reddit.subreddit(term).top(limit=params)

    def get_posts_info(self, term, qty):
        result = {}
        search_result = self.search_subreddit(term, qty)
        for term in search_result:
            if term.author not in list(result.keys()):
                result[term.author] = []

            result[term.author] = {'id': term.id,
                                   'title': term.title,
                                   'text': term.selftext,
                                   'comments': term.comments.list(),
                                   'url': term.url}
        return result

test = RedditTarget()
test.get_posts_info('anxiety')
