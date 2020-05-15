import tweepy as tw
import pandas as pd
import json
from TwitterAPI import TwitterAPI

# App Auth
consumer_key = 'XXX'
consumer_secret = 'XXX'
access_key = 'XXX'
access_secret = 'XXX'

api =  TwitterAPI(consumer_key,consumer_secret,access_key,access_secret)
r = api.request('statuses/filter', {'locations':'-171.791110603, 18.91619, -66.96466, 71.3577635769'})

tweets_arr = [0 for i in range(250000)]
j = 0
for item in r:
    tweets_arr[j] =item
    j += 1

# check = tweets_arr[50000:51000]

with open("data_US_2.json", "w+") as output:
    output.write(json.dumps(tweets_arr))