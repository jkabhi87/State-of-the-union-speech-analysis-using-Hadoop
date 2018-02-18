#!/usr/bin/env python
import sys

# maps words to their counts
wordmax = {}
wordmin = {}
#wordmin = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
#    year, wordcount = line.split('\t',1)
    # convert count (currently a string) to int
    word, count = line.split('\t',1)
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        if wordmax[word] < count :
            wordmax[word] = count
    except:
        wordmax[word] = count

    try:
        if wordmin[word] > count :
            wordmin[word] = count
    except:
        wordmin[word] = count

# write the tuples to stdout
# Note: they are unsorted
for word in wordmax.keys() :
    print '%s\t%s\t%s'% ( word, wordmax[word],wordmin[word])
