#First read in the data from the text file, soon we will be reading from social media
test_str = open("gmrTweets.txt").read()
test_dic = eval(test_str)
print test_dic["text"]

# loop thru all the keys in the outer layer of the dict
for key in test_dic:
    print key

# iterate thru the values for the keys
for key in test_dic:
    print key, test_dic[key]

# let's check the type of each value to see if it's a dict or list
for key in test_dic:
    print key, isinstance(test_dic[key],dict)

# iterate over dic "user"
for key in test_dic["user"]:
    print "user",key,test_dic["user"][key]

# see the lenghts of each set of lists
for key in test_dic["entities"]:
    print "entities",key,isinstance(test_dic["entities"][key],list),len(test_dic["entities"][key])

# look at a fourth layer of complex data type
for key in test_dic["entities"]["urls"][0]:
    print "entities urls", key, test_dic["entities"]["urls"][0][key]

print test_dic["entities"]["urls"][0]["display_url"]
