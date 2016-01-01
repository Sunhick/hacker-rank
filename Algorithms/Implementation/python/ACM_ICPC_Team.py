#!/bin/python

import sys

#binary = lambda n: '' if n==0 else binary(n/2) + str(n%2)

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in xrange(n):
   topic_t = str(raw_input().strip())
   topic.append(topic_t)

maxTopics = 0
totalPeople = []
for x in range(0,len(topic)-1):
    for y in range(x,len(topic)):
        interSection = str(bin(int(topic[x],2) | int(topic[y],2))).split('b')[1]
        #print interSection
        totalPeople.append(interSection)
        maxTopics = max(maxTopics,interSection.count('1') )

print maxTopics

count = 0 
for y in range(0,len(totalPeople)):
    if ( totalPeople[y].count('1') == maxTopics ):
        count += 1
        
print count
