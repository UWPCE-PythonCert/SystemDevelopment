#!/usr/bin/env python3

"""
some quick processing of the survey for the third class
"""

pref_map = { '': -1,
             'Not at all':0,
             'Not much':1,
             'Somewhat':2,
             'Very':3,
             }

with open("Python 3 Topic Options (Responses) - Form Responses 1.tsv") as infile:
    topics = infile.readline().strip().split('\t')[1:]
    topics = [line.split('[')[1].rstrip(']') for line in topics]
    data_table = [[pref_map[pref.strip()] for pref in line.split('\t')[1:]] for line in infile]

results = []
for i, topic in enumerate(topics):
    #get the average for that topic
    scores = [row[i] for row in data_table if row[i] >= 0]
    results.append(sum(scores) / len(scores))
results = sorted(zip(topics, results), key= lambda x: -x[1])

with open("survey_results.txt", 'w') as outfile:
    for topic, score in results:
        line = "%50s %.2f"%(topic,score)
        outfile.write(line+'\n')
        print(line)




