# State-of-the-union-speech-analysis-using-Hadoop
Using Hadoop's MapReduce to analyze "State of the union" addresses

1. mapper_yearly_avg.py - python mapper script to calculate average word usage per year.
2. reducer_yearly_avg.py - python reducer script to calculate average word usage per year.
3. mapper_wordminmax.py - python mapper script to calculate maximum and minimum times a word appears in all of the speeches.
4. reducer_wordminmax.py - python mapper script to calculate maximum and minimum times a word appears in all of the speeches.
5. mapper_avg_sd.py - python mapper script to calculate average and standard deviation of times a word appears in 4 year window.
6. reducer_avg_sd.py - python reducer script to calculate average and standard deviation of times a word appears in 4 year window.
7. mapper_words_above_avg_2sd.py - python mapper script to find the words that appear more frequently than avergare+2 standard deviation in the preceding 4 year window.
8. reducer__words_above_avg_2sd.py - python reducer script to find the words that appear more frequently than avergare+2 standard deviation in the preceding 4 year window.
9. pseudocode_yearly_average.txt - pseudocode for average word usage per year.
10. pseudocode_wordminmax.txt - pseudocode for calculating maximum and minimum times a word appears in all the speeches.
11. pseudocode_avg_standard_deviation.txt - pseudocode for calculating average and standard deviation of times a word appears in 4 year window.
12. pseudocode_words_above_avg_2sd.txt - pseudocode to find the words that appear more frequently than avergare+2 standard deviation in the preceding 4 year window.
13. sampleoutput_averagewordusageperyear.txt - sample output of average word usage per year.
14. sample_output_wordminmax.txt - sample output of maximum and minimum times a word appears in all of the speeches.
15. sampleoutput_word_avd_standarddev.txt - sample output of average and standard deviation of times a word appears in 4 year window.
16. 2017.txt - output of the words that appear more frequently than avergare+2 standard deviation in the preceding 4 year window of 2013-2016.
17. scraper.py - python script to fetch the data from the website.
18. removepunc.py - python script that removes the punctuations from the text files.
19. stopper.py - python script for stopword removal from all the text files of the speeches.
20. Runtime_chart.png - graph for runtime comparison with the file size.
