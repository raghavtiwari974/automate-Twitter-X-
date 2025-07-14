import tweepy


API_KEY = 'YOUR_API_KEY'
API_SECRET = 'YOUR_API_SECRET'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'


auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


tweet = " Hello, Twitter! This tweet was posted using Python. #Python #TwitterAPI"

try:
    api.update_status(tweet)
    print(" Tweet posted successfully!")
except Exception as e:
    print(" Failed to post tweet:", e)
