import sys
import math

for line in sys.stdin:
    line = line.strip()
    #read the word, its avg+2sd, word count in the 5th year.
    word,avg2sd,count = line.split('\t', -1)
    try:
        avg2sd = float(avg2sd)
        count = float(count)
    except ValueError:
        continue
    
    #if the wordcount is more than the avg+2sd, then print the word, else continue.
    if(count > avg2sd) :
        print(word)
    else:
        continue
