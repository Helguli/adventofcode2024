#!/bin/env python

def getMiddleNumberOrder(pages):
    corrected = False
    for x in range(len(pages) - 1):
        y = x + 1
        while y < len(pages):
            first = pages[x]
            second = pages[y]
            if first not in rules or second not in rules[first]:
                pages[x] = second
                pages[y] = first
                corrected = True
                continue
            y += 1
    return pages[int((len(pages) / 2))] if corrected else 0

def getMiddleNumber(pages):
    for x in range(len(pages) - 1):
        for y in range(x + 1, len(pages)):
            first = pages[x]
            second = pages[y]
            if first not in rules or second not in rules[first]:
                return 0
    return pages[int((len(pages) / 2))]

f = open("input05", "r")

rules = {}

input_rules = True

summiddle = 0

for line in f:
    if line == "\n":
        input_rules = False
        continue
    #print(line)
    if input_rules:
        rule = line.split('|')
        first = int(rule[0])
        second = int(rule[1])
        if first in rules:
            rules[first].add(second)
        else:
            rules[first] = set()
            rules[first].add(second)
    else:
        pages = [int(x) for x in line.split(",")]
        print(pages)
        #summiddle += getMiddleNumber(pages)
        summiddle += getMiddleNumberOrder(pages)


print(summiddle)
#print(rules)
        
