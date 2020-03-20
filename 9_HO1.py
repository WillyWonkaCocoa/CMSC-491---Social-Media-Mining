import json
import pymongo
import sys
try:
    conn = pymongo.MongoClient('localhost:27017')
    db = conn.cmsc491
except pymongo.erros.ConnectionFailure as e:
    print "problem connecting to cmsc461", e
    sys.exit(1)

#Get control set of tweets
hlc = db.antarctica
tweets = hlc.find()

#Show number of tweets in this cursor
print "Number of tweets", tweets.count()

#Look at the first tweet
print tweets[0]["id"]

#Display the values of language
print "The lanugate for this tweet is", tweets[0]["lang"]
print "The like count is", tweets[0]["favorite_count"]
print "The body of the message:", tweets[0]["text"].encode('utf-8')

#Loop through the cursor
for tweet in tweets:
    print tweet["id"]
