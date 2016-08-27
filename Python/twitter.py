import tweepy

consumer_key = 'RzUX2MvvQUYBsdfRqRXXUJaa8'
consumer_secret = 'csXhxH79s2RTzM8zYmCiEhAiYjKjQuGhfCZBaKpyEu5zLy6VXs'
access_token = '196919500-ejqw4Nk6mtS7ttSNjG7tmReRfRAwYXKHMt5ww2yo'
access_token_secret = 'Xx20esEUu8runa4722n6EiQke3r87BoJkfwEaWw84rqtH'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

results = api.search(q="kesgrave",lang="en",count=100,geocode="52.0567,1.1482,200km")
print len(results)
raw_input()
for result in results:
    print result.text
    raw_input()

