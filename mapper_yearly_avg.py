#!/usr/bin/env python
import sys
import os
#import collections

#wrdcnt = collections.Counter()
#--- get all lines from stdin ---
for line in sys.stdin:
    #get the year based on the input file name.
    inputfile = os.environ['mapreduce_map_input_file'].split('/')[-1]
    inputfile = inputfile[:4]
    #--- remove leading and trailing whitespace---
    line = line.strip()

    #--- split the line into words ---
    words = line.split()

    #--- output tuples [year,word, 1] in tab-delimited format---
    for word in words:
        print(inputfile+"\t"+word+"\t"+"1")

