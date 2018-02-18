#!/usr/bin/env python
import sys
import os

wordcount = {}
wordavg2sd = {}

#inputfile = os.environ['mapreduce_map_input_file']
#--- get all lines from stdin ---
for line in sys.stdin:
    #inputfile ="asasd"
    
    #get the year based on the input file name.
    inputfile = os.environ['mapreduce_map_input_file'].split('/')[-1]
    inputfile = inputfile[0:4]
    #--- remove leading and trailing whitespace---
    line = line.strip()
    
    if inputfile == "2017" : #change this value based on the 5th year requirement.
        word , count = line.split('\t',1)
        try:
            count = int(count)
        except ValueError :
            continue
        
        wordcount[word] = count
    else:	#if this is the file with avg and std dev values, then read 3 values per line.
        word,avg,sd = line.split('\t',-1)
        try:
            avg = float(avg)
            sd = float(sd)
        except ValueError :
            continue
        
        try:
            wordavg2sd[word] = avg + (2 * sd) #calculate the average _ 2*std_dev for each word.
        except :
            continue

for word in wordcount.keys() : #this is just to set the values to 0 if the value isnt present.
    try:
       wordavg2sd[word] = wordavg2sd[word] * 1.0
    except:
       wordavg2sd[word] = 0.0 

for word in wordcount.keys() :
    print(word+"\t"+str(wordavg2sd[word])+"\t"+str(wordcount[word]))
