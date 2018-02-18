#!/usr/bin/env python
import sys
from itertools import product

# maps words to their counts
word2count = {} #count of each word in a year
totalwordcount = {} #total word count in a given year
allwords = {} # keeps track of all words that were encountered.
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    year, word, count = line.split('\t',-1)
    # convert count (currently a string) to int
	
    try:
        count = int(count)
    except ValueError:
        continue
    
    try:
        allwords[word] = 1
    except:
        allwords[word] = 1
    
    try:
        word2count[(year,word)] = word2count[(year,word)]+count
    except:
        word2count[(year,word)] = count
    
    try:
        totalwordcount[year] = totalwordcount[year] + count
    except:
        totalwordcount[year] = count

#if the word doesnt appear in a year, set the word count to 0.
for year,word in product(totalwordcount.keys(), allwords.keys()):
    try:
        word2count[(year,word)] = word2count[(year,word)]
    except:
        word2count[(year,word)] = 0

#print word and it's average usage for that year.
for year,word in product(totalwordcount.keys(), allwords.keys()):
    print (year+"\t"+word+"\t"+str(word2count[(year,word)]/(totalwordcount[year] * 1.0)) )


