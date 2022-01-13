import tweepy
 
import pandas as pd
import csv
import re 
import string
import preprocessor as p
 
 # Enter you keys
consumer_key = ""
consumer_secret = ""
access_key= ""
access_secret = ""
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
 
api = tweepy.API(auth,wait_on_rate_limit=True)
 
csvFile = open('tourismindiah.csv', 'a')
csvWriter = csv.writer(csvFile)
 
search_words = "tourismgoi"      # enter your words
new_search = search_words + " -filter:retweets"
 
for tweet in tweepy.Cursor(api.search_tweets,q=new_search,count=100,
                           lang="en",
                           since_id=0).items(1000):
    # tweet = re.sub("@[A-Za-z0-9]+","",tweet) #Remove @ sign
    # tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet) #Remove http links
    # tweet = " ".join(tweet.split())
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])
