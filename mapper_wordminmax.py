#!/usr/bin/env python
import sys
import collections

#inputfile = os.environ['mapreduce_map_input_file']
#wrdcnt = collections.Counter()
#--- get all lines from stdin ---
for line in sys.stdin:
    #--- remove leading and trailing whitespace---
    line = line.strip()

    #--- split the line into words ---
    word, count = line.split('\t',1)

    print '%s\t%s' % (word, count)

#for key,value in wrdcnt.items
