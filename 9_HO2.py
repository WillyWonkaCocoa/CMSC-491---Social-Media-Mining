import json
import pymongo
import sys
try:
    conn = pymongo.MongoClient('localhost:27017')
    db = conn.cmsc491
except pymongo.errors.ConnectionFailure as e:
    print "problem connecting to cmsc491",e
    sys.exit(1)
hlc = db.antarctica
tweets = hlc.find()
for item in tweets[0]["entities"]:
    print item, tweets[0]["entities"][item]

print "==============================="

#Go into user_mentions
if tweets[0]["entities"]["user_mentions"]:
    for field in tweets[0]["entities"]["user_mentions"]:
        print field
    print "==============================="

    #Get a particular ID
    print tweets[0]["entities"]["user_mentions"][0]["id_str"]
else:
    print "no user mentions this go round"

print " "
if tweets[0]["entities"]["urls"]:
    print tweets[0]["entities"]["urls"]
else:
    print "NO URLS this go round"
print " "

#Select a particular hashtag text
if tweets[0]["entities"]["hashtags"]:
    print tweets[0]["entities"]["hashtags"][0]["text"]
else:
    print "NO hashtags this go round"
