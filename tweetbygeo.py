import tweepy
import os
import json
import sys
import geocoder

# API Keys and Tokens
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Authorization and Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

if __name__ == "__main__":
    # Available Locations
    available_loc = api.available_trends()
    # writing a JSON file that has the available trends around the world
    with open("available_locs_for_trend.json","w") as wp:
        wp.write(json.dumps(available_loc, indent=1))

    # Trends for Specific Country
    loc = sys.argv[1]     # location as argument variable 
    g = geocoder.osm(loc) # getting object that has location's latitude and longitude

    closest_loc = api.closest_trends(g.lat, g.lng)
    trends = api.get_place_trends(closest_loc[0]['woeid'])
    # writing a JSON file that has the latest trends for that location
    with open("twitter_{}_trend.json".format(loc),"w") as wp:
        wp.write(json.dumps(trends, indent=1))