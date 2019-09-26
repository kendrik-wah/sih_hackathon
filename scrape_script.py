from instagram_infiltrate import InstagramScrape
from twitter_infiltrate import TwitterTarget
from reddit_scrape import RedditTarget
import json


def scrape():
    instagram_handle = InstagramScrape('xxx', 'xxx')
    twitter_handle = TwitterTarget('ChaotiqueEdge')
    reddit_handle = RedditTarget()
    mental_illnesses = ['depression', 'anxiety', 'stress']

    instagram_handle.scrape(mental_illnesses)
    twitter_handle.scrape(mental_illnesses)
    reddit_handle.scrape(mental_illnesses)


def read_json_file(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def get_instagram_json(file):
    data = read_json_file(file)
    key = list(data.keys())[0]
    return data[key]


def get_twitter_json(file):
    data = read_json_file(file)
    return data


def get_reddit_json(file):
    data = read_json_file(file)
    return data


def get_top_5_texts(lst):
    all_recorded_users = []
    texts = {}
    use_id = True

    try:
        val = lst[0]['id']
    except KeyError as ke:
        use_id = False


    if use_id is True:
        all_recorded_users_double_counted = list(map(lambda x: x['id'], lst))

        for user in all_recorded_users_double_counted:
            if user not in all_recorded_users:
                all_recorded_users.append(user)

        for user in all_recorded_users:
            filtered = list(filter(lambda x: x['id'] == user, lst))
            top_5 = list(filter(lambda x: len(x['text']) != 0, filtered))

            if len(top_5) > 5:
                top_5 = top_5[0:5]

            texts[user] = top_5
    else:
        all_recorded_users_double_counted = list(map(lambda x: x['author'], lst))

        for user in all_recorded_users_double_counted:
            if user not in all_recorded_users:
                all_recorded_users.append(user)

        for user in all_recorded_users:
            filtered = list(filter(lambda x: x['author'] == user, lst))
            top_5 = list(filter(lambda x: len(x['text']) != 0 or len(x['title']) != 0, filtered))

            if len(top_5) > 5:
                top_5 = top_5[0:5]

            texts[user] = top_5

    return texts


instagram_depression = get_top_5_texts(get_instagram_json('instagram_depression.json'))
instagram_anxiety = get_top_5_texts(get_instagram_json('instagram_anxiety.json'))
instagram_stress = get_top_5_texts(get_instagram_json('instagram_stress.json'))

twitter_depression = get_top_5_texts(get_twitter_json('twitter_depression.json'))
twitter_anxiety = get_top_5_texts(get_twitter_json('twitter_anxiety.json'))
twitter_stress = get_top_5_texts(get_twitter_json('twitter_stress.json'))

reddit_depression = get_top_5_texts(get_reddit_json('reddit_depression.json'))
reddit_anxiety = get_top_5_texts(get_reddit_json('reddit_anxiety.json'))
reddit_stress = get_top_5_texts(get_reddit_json('reddit_stress.json'))


