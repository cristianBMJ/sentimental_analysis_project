import tweepy
import pandas as pd

# Twitter API credentials
consumer_key = 'JF4VjgeYd1b5xu7BXeeu9LRNK'
consumer_secret = 'EpXebQ4Za7xJ82FuYurGgp8oGcoCjE6YTNDVoCiqS9FcyQtM2Q'
access_token = '1778082559768846336-rbNoHoPyC7NC32QRMJs95vXuoABr23'
access_token_secret = 'hHwmjLrwU6MLIbtaiWuYA1U1K0eVsgy6DzbxUHdabfWgM'

# Authenticate
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def scrape_tweets(query, num_tweets):
    tweets = []
    for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode='extended').items(num_tweets):
        tweets.append(tweet.full_text)
    return tweets

if __name__ == "__main__":
    query = input("Enter search query: ")
    num_tweets = int(input("Enter number of tweets to scrape: "))
    tweets = scrape_tweets(query, num_tweets)
    df = pd.DataFrame({'tweets': tweets})
    df.to_csv('../data/raw_data/tweets.csv', index=False)
    print("Tweets saved to tweets.csv")
