#!/bin/env python

f = open("input01", "r")
list1 = []
list2 = []
for x in f:
    y = x.split()
    list1.append(int(y[0]))
    list2.append(int(y[1]))
list1.sort()
list2.sort()

print(list1)
print(list2)

distsum = 0

for i in range(len(list1)):
    distsum += abs(list1[i]-list2[i])

print(distsum)

from functools import reduce

similaritysum=0

counts = reduce(
    lambda acc, num: {**acc, num: acc.get(num, 0) + 1}, 
    list2, 
    {}
)

for x in list1:
    if x in counts:
        similaritysum += counts[x] * x

print(similaritysum)
