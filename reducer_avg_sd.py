#!/usr/bin/env python
import sys
import math
from itertools import product

# maps words to their counts
word2count = {}
allwords = {}
totalwordcount = {}
sumofdiff = {}
stdev = {}
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    year, word,count = line.split('\t', -1)

    try:
        allwords[word] = 1 #if a word is found in any document, just set this to 1 representing that the word was seen.
    except:
        allwords[word] = 1

#    word, count = wordandcount.split('\t',1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        word2count[(year,word)] =  count #word count for every year.
    except :
        continue

    try:
        totalwordcount[word] = totalwordcount[word] + count #word count of a specific word for all 4 years.
    except:
        totalwordcount[word] = count

#print(word2count)
# write the tuples to stdout
# Note: they are unsorted
for year,word in product(range(2013,2016),allwords.keys() ): #change the range to the period of 4 years you want.
    try:
        word2count[(year,word)] = word2count[(year,word)] #check if there is a word count for a word in a given year.
    except :
        word2count[(year,word)] = 0 # if word isnt found in a year, set it to 0.

#please note that i have not used additional array for storing average values. I am reusing the totalwordcount array for it.
for word in allwords.keys():
    totalwordcount[word]= totalwordcount[word]/(4*1.0) #calculate the average word usage for 4 years.

#once we have the average, calculate the standard deviation in multiple steps by computing individual components involved.
#the following for loop calculates sum of all (x-avg(x))^2.
for year,word in product(range(2013,2016),allwords.keys() ):
    try:
        sumofdiff[word] = sumofdiff[word] + ((word2count[(year,word)]-totalwordcount[word])*(word2count[(year,word)]-totalwordcount[word]))
    except:
        sumofdiff[word] = ((word2count[(year,word)]-totalwordcount[word])*(word2count[(year,word)]-totalwordcount[word]))

#now calculate std deviation
for word in allwords.keys():
    sumofdiff[word] = sumofdiff[word]/(4*1.0)
    stdev[word] = math.sqrt(sumofdiff[word])

#please note that i have not used additional array for storing average values. I am reusing the totalwordcount array for it.
for word in allwords.keys() :
    print(word+"\t"+str(totalwordcount[word])+"\t"+str(stdev[word]))
