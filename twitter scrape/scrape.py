# Before scraping tweets using Python, you need access via Twitter's API. This access is easily attainable through Twitter's developer platform https://developer.twitter.com/en.

!pip install tweepy
import tweepy

# Input API credentials from Twitter app developer account
consumer_key= 'insert'
consumer_secret= 'insert'
access_token= 'insert'
access_token_secret= 'insert'

# Create an OAuthHandler instance and pass keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

# Scrape tweets from a user's account
posts = api.user_timeline(screen_name = "@user", count = 7, lang ="en", tweet_mode="extended")

# Create dataframe
df = pd.DataFrame(data =[tweet.text for tweet in posts], columns = ["Tweet"])
