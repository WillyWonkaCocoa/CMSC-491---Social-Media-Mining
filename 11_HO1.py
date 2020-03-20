import json
import pymongo
import sys
from collections import Counter
from prettytable import PrettyTable
try:
    conn = pymongo.MongoClient('localhost:27017')
    db = conn.cmsc491
except pymongo.errors.ConnectionFailure as e:
    print "problem connecitng to cmsc491", e
    sys.exit(1)

#create and execute query
hlc = db.antarctica
tweets = hlc.find()
g = open('gmrTweet.txt','w')

#create list of typles for the fields we have an interest
retweets = []

#loop trhu statues
for status in tweets:
    if 'retweeted_status' in status:
        retweets.append((status['user']['screen_name'],
                         status['retweeted_status']['user']['screen_name'],status['text']))
        g= open('gmrText.txt', 'w')
        g.write(str(status)) #write tweeet with 'retweeted_status' to a file 
        g.close()

pt = PrettyTable(filed_names=['Usr','rtUsr','Text'])
[pt.add_row(row) for row in sorted(retweets, reverse=True)[:5]]
pt.max_width['Text'] = 40
pt.algin = 'l'
print pt
