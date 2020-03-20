import pymongo
import sys
import json

try:
    conn = pymongo.MongoClient('localhost:27017')
    db = conn.cmsc491
except pymongo.errors.ConnectionFailure as e:
    print "problem connecting to cmsc491", e
    sys.exit(1)

def loadData(fileName, hlc):
    in_str = open(fileName).read()
    in_lst = eval(in_str)
    for tweet in in_lst:
        if "text" in tweet:
            print tweet["text"].encode('utf-8')
            hlc.insert(tweet)
    print "Length is",len(in_lst)
    return;
    
#load in Antarctica data
hlc = db.antarctica
loadData("Antarctica.txt",hlc)

#load in Coca Cola data
hlc = db.CocaCola
loadData("CocaCola.txt",hlc)

#load in Brett Kavanaugh data
hlc = db.Kavanaugh
loadData("Kavanaugh.txt",hlc)

#load in Pepsi data
hlc = db.pepsi
loadData("Pepsi.txt",hlc)

#load in Raspberry Pi data
hlc = db.raspberry
loadData("raspberry.txt",hlc)

#load in Tariffs data
hlc = db.tariffs
loadData("tariffs.txt",hlc)
