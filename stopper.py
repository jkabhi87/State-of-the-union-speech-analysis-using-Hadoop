import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import os

def stopper(filename):
  input_file = open(filename,"r")
  output_file = open(filename[:-6],"w")
#  stop_words = set(stopwords.words("english"))
  for line in input_file:
    line_words = word_tokenize(line)
    no_stop_words = list()
    for x in line_words:
      if x not in stopwords.words('english'):
        no_stop_words.append(x)
      else:
        continue
    stopped_string = (' '.join(no_stop_words))
    output_file.write(stopped_string)
    output_file.write("\n")
  input_file.close()
  output_file.close()


for f in os.listdir('/Users/abhishek/Desktop/HW1/stopped_data/'):
    stopper(f)
