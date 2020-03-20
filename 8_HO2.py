import pymongo
import sys
import json
try:
    conn = pymongo.MongoClient('localhost:27017')
    db = conn.cmsc491
except pymongo.errors.ConnectionFailure as e:
    print "problem connecting to cmsc491",e
    sys.exit()

#connect to a collection
hlc=db.antarctica

#retrieve the tweets in that collection
results = hlc.find()

#print results
for tweet in results:
    print tweet["text"].encode('utf-8'), tweet["user"]["followers_count"]
    print "---\n"
