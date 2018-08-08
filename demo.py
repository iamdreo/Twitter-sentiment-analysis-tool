import tweepy
from textblob import TextBlob
import numpy as np
import operator

# Step 1 - Authenticate
consumer_key= ''
consumer_secret= ''

access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('gulder')

#Step 2 - Prepare query features

#List of candidates to French Republicans Primary Elections
Brand_name = 'Konga'
#Hashtag related to the debate
Hashtag = "#blackfriday" 
#Date of the debate : October 13th
since_date = "2017-10-1"
until_date = "2017-11-1"


#Step 2b - Function of labelisation of analysis
def get_label(analysis, threshold = 0):
	if analysis.sentiment[0]>threshold:
		return 'Positive'
	elif analysis.sentiment[0] == threshold:
		 return 'neutral'
	else:
		return 'Negative'
#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


all_polarities = dict()
for brand in Brand_name:
	this_brand_polarities = []
	this_brand_tweets = api.search(q='Globacom', count=50, lang='en')
	#Save the tweets in csv
	with open('%s_tweets.csv' % brand, 'wb') as this_brand_file:
		this_brand_file.write('tweet,sentiment_label\n')
		for tweet in this_brand_tweets:
			analysis = TextBlob(tweet.text)
			#Get the label corresponding to the sentiment analysis
			this_brand_polarities.append(analysis.sentiment[0])
			this_brand_file.write('%s,%s\n' % (tweet.text.encode('utf8'), get_label(analysis)))
 