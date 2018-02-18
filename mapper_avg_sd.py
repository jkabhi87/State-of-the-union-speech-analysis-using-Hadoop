#!/usr/bin/env python
import sys
import os

#--- get all lines from stdin ---
for line in sys.stdin:
    #inputfile ="asasd"
    #--- remove leading and trailing whitespace---
    #get the year based on the input file name.
    inputfile = os.environ['mapreduce_map_input_file'].split('/')[-1]
    inputfile = inputfile[0:4]
    line = line.strip()

    #--- split the line into words ---
    word , count = line.split('\t',1)

    #--- output tuples [word, count] in tab-delimited format---
    for word in words:
        print(inputfile+"\t"+word+"\t"+str(count))
