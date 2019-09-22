from InstagramAPI import InstagramAPI

user_name = 'kendrikwah'
password = 'flairbomber'

acc = InstagramAPI(username=user_name, password=password)

acc.login()

acc.getProfileData()
profile_data = acc.LastJson
print(profile_data)

acc.getSelfUserFeed()
user_feed = acc.LastJson
print(user_feed)

acc.getRecentActivity()
recent_activity = acc.LastJson
print(recent_activity)

acc.getSelfSavedMedia()
saved_media = acc.LastJson
print(saved_media)

