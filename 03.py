#!/bin/env python

import re


f = open("input03", "r")

do = True

mulsum = 0

data = f.read()
x = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)
for y in x:
    if y == "do()":
        do = True
    elif y == "don't()":
        do = False
    elif do:
        z = y.split("(")[1].split(")")[0].split(",")
        mulsum += int(z[0])*int(z[1])
    
print(mulsum)
