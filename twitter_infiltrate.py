import twitter

class TwitterTarget(object):

    def __init__(self):
        self.consumer_API_key = "8mo1oe5PCYxRzXytj8lK9beaM"
        self.consumer_secret_API_key = "E7l6T7MYBCn05YGLA05tfVz9NKIfBNKJR79JjxALntnr6je113"
        self.access_token = "805220750042857472-n3zPdbfnjMLn1QpWV7igz42vG7Eqrvz"
        self.secret_access_token = "c19vA2yQQ0a0gYhMpcKzAehi6vKgJLUSZMFzVuYjEOchT"
        self.api = twitter.Api(consumer_key=self.consumer_API_key,
                               consumer_secret=self.consumer_secret_API_key,
                               access_token_key=self.access_token,
                               access_token_secret=self.secret_access_token)
        self.username = None
        self.search_result = {}
        self.target_user_result = None
        self.results = {}

    def search_by_parameter(self, parameter):
        results = self.api.GetUsersSearch(term=parameter)
        for result in results:
            if result.id not in list(self.search_result.keys()):
                self.search_result[result.id] = ''
            self.search_result[result.id] = result.screen_name
        return self.search_result

    def set_target_by_username(self, username):
        self.username = username
        self.target_user_result = self.api.GetUserTimeline(screen_name=self.username,
                                                           count=200)

        for status in self.target_user_result:
            id = status.id
            name = status.user.screen_name
            time = status.created_at
            text = status.text
            hashtags = status.hashtags
            media = status.media

            if 'RT' in text:
                other_party = ""
                take_in = False
                count = 0
                for character in text:
                    if character == '@':
                        take_in = True
                        count = count + 1
                    elif character == ':':
                        text = text[count:]
                        name = other_party
                        break
                    elif take_in:
                        other_party = other_party + character
                        count = count + 1
                    elif not take_in:
                        count = count + 1
                        continue

            if name not in list(self.results.keys()):
                self.results[name] = []
            self.results[name].append({"id": id,
                                       "body": text,
                                       "time": time,
                                       "hashtags": hashtags,
                                       "media": media})

    def get_results(self):
        return self.results

    def get_tweeters(self):
        return list(self.results.keys())

test = TwitterTarget()

###############################################################################################################
# Use search_by_parameters to obtain 20 usernames. Only the same 20 will always be obtained.                  #
# For example, if I intend to look for depression, use test.search_by_parameter('depression') as shown below. #
###############################################################################################################
# search_depression = test.search_by_parameter('depression')

######################################################################################################################
# Use set_target_by_username to obtain the last 200 posts of that username.                                          #
# Refer below for an example. It may be helpful to use the get_tweeters() method to see who made posts in that page. #
# Use get_results() method to get direct access to the results. It is a dictionary.                                  #
######################################################################################################################
# test.set_target_by_username("BeyondBrokenDep")
# print(test.get_results())




