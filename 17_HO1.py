import russell as ru
from bs4 import  BeautifulSoup
import requests
import json
import codecs
import nltk

#Routine to remove unicode characters
def removeUnicode(text):
    asciiText=""
    for char in text:
        if(ord(char) < 128):
            asciiText=asciiText+char
    return asciiText

fileObj = codecs.open("17_HO1.rtf","w","UTF")
html = requests.get("http://swe.umbc.edu/~rayg/econ_plan.html")
soup = BeautifulSoup(html.text, 'html5lib')
all_paras = soup.find_all('p')

#write text to file and colalte it into a str var
data_2018 = ""
for para in all_paras:
    fileObj.write(para.text)
    data_2018 = data_2018 + para.text

iceberg_sum = ru.summarize(data_2018)
print "Summary of economic plan"
print "Print Three Sentence Summary"
for sent in iceberg_sum['top_n_summary']:
    print removeUnicode(sent)

asc_2018 = removeUnicode(data_2018)
bigWords = nltk.tokenize.word_tokenize(asc_2018)
N = 25
search = nltk.BigramCollocationFinder.from_words(bigWords)
search.apply_freq_filter(2)
search.apply_word_filter(lambda skips: skips in nltk.corpus.stopwords.words('English'))
from nltk import BigramAssocMeasures
idxJaccard = BigramAssocMeasures.jaccard
bigrams = search.nbest(idxJaccard, N)
for bigram in bigrams:
    print str(bigram[0]).encode('utf-8'),"",str(bigram[1]).encode('utf-8')
