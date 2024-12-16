#!/bin/env python

f = open("input06", "r")

data0 = f.read().split("\n")
del data0[-1]
rows = len(data0)
cols = len(data0[0])

xpos = 0
ypos = 0
direction = ""
xstart = 0
ystart = 0

data = []
for i, r in enumerate(data0):
    if '^' in r or 'v' in r or '<' in r or '>' in r:
        xpos = r.find('^')
        ypos = i
        xstart = xpos
        ystart = ypos
        direction = "up"
    data.append(list(r))

"""
while True:
    if direction == "up" and ypos > 0:
        if data[ypos - 1][xpos] != '#':
            data[ypos][xpos] = "X"
            ypos -= 1
        else:
            print("right turn", ypos, xpos)
            direction = "right"
    elif direction == "down" and ypos < len(data) - 1:
        if data[ypos + 1][xpos] != '#':
            data[ypos][xpos] = "X"
            ypos += 1
        else:
            print("left turn", ypos, xpos)
            direction = "left"
    elif direction == "left" and xpos > 0:
        if data[ypos][xpos - 1] != '#':
            data[ypos][xpos] = "X"
            xpos -= 1
        else:
            print("up turn", ypos, xpos)
            direction = "up"
    elif direction == "right" and xpos < len(data[0]) - 1:
        if data[ypos][xpos + 1] != '#':
            data[ypos][xpos] = "X"
            xpos += 1
        else:
            print("down turn", ypos, xpos)
            direction = "down"
    else:
        data[ypos][xpos] = "X"
        print(xpos, ypos)
        break

counter = 0
for r in data:
    for c in r:
        if c == "X":
            counter += 1
print(counter)
"""

obsx = 0
obsy = 0

def possibleWay(xpos, ypos, direction):
    data2 = []
    for x in data:
        a = []
        for y in x:
            a.append(y)
        data2.append(a)
    data2[ypos][xpos] = "."

    while True:
        if direction == "up" and ypos > 0:
            if data2[ypos][xpos] == "^":
                return True
            if data2[ypos - 1][xpos] != '#':
                data2[ypos][xpos] = "^"
                ypos -= 1
            else:
                direction = "right"
        elif direction == "down" and ypos < len(data2) - 1:
            if data2[ypos][xpos] == "v":
                return True
            if data2[ypos + 1][xpos] != '#':
                data2[ypos][xpos] = "v"
                ypos += 1
            else:
                direction = "left"
        elif direction == "left" and xpos > 0:
            if data2[ypos][xpos] == "<":
                return True
            if data2[ypos][xpos - 1] != '#':
                data2[ypos][xpos] = "<"
                xpos -= 1
            else:
                direction = "up"
        elif direction == "right" and xpos < len(data2[0]) - 1:
            if data2[ypos][xpos] == ">":
                return True
            if data2[ypos][xpos + 1] != '#':
                data2[ypos][xpos] = ">"
                xpos += 1
            else:
                direction = "down"
        else:
            #print(ypos, xpos)
            return False



obstacles = set()

while True:
    if direction == "up" and ypos > 0:
        if data[ypos - 1][xpos] != '#':
            if data[ypos - 1][xpos] != 'o':
                data[ypos - 1][xpos] = '#'
                if possibleWay(xstart, ystart, "up"):
                    obstacles.add((xpos, ypos -1))
                    obsx = xpos
                    obsy = ypos - 1
                    data[ypos - 1][xpos] = 'o'
                else:
                    data[ypos - 1][xpos] = '.'
            ypos -= 1
        else:
            print("right turn", ypos, xpos)
            direction = "right"
    elif direction == "down" and ypos < len(data) - 1:
        if data[ypos + 1][xpos] != '#':
            if data[ypos + 1][xpos] != 'o':
                data[ypos + 1][xpos] = '#'
                if possibleWay(xstart, ystart, "up"):
                    obstacles.add((xpos, ypos +1))
                    obsx = xpos
                    obsy = ypos + 1
                    data[ypos + 1][xpos] = 'o'
                else:
                    data[ypos + 1][xpos] = '.'
            ypos += 1
        else:
            print("left turn", ypos, xpos)
            direction = "left"
    elif direction == "left" and xpos > 0:
        if data[ypos][xpos - 1] != '#':
            if data[ypos][xpos - 1] != 'o':
                data[ypos][xpos - 1] = '#'
                if possibleWay(xstart, ystart, "up"):
                    obstacles.add((xpos - 1, ypos))
                    obsx = xpos - 1
                    obsy = ypos
                    data[ypos][xpos - 1] = 'o'
                else:
                    data[ypos][xpos - 1] = '.'
            xpos -= 1
        else:
            print("up turn", ypos, xpos)
            direction = "up"
    elif direction == "right" and xpos < len(data[0]) - 1:
        if data[ypos][xpos + 1] != '#':
            if data[ypos][xpos + 1] != 'o':
                data[ypos][xpos + 1] = '#'
                if possibleWay(xstart, ystart, "up"):
                    obstacles.add((xpos + 1, ypos))
                    obsx = xpos + 1
                    obsy = ypos
                    data[ypos][xpos + 1] = 'o'
                else:
                    data[ypos][xpos + 1] = '.'
            xpos += 1
        else:
            print("down turn", ypos, xpos)
            direction = "down"
    else:
        print(xpos, ypos)
        break


to_print = ["".join(x) for x in data]
print("\n".join(to_print))

print(obstacles)
print(len(obstacles))

counter = 0
for r in data:
    for c in r:
        if c == "o":
            counter += 1
print(counter)

print(xpos, ypos)
