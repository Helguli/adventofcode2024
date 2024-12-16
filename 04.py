#!/bin/env python

f = open("input04", "r")

data = f.read().split("\n")
data.pop()
print(data)

counter = 0

print(data)
for r,y in enumerate(data):
    print(y)
    for c,x in enumerate(y):
        print(r, c)
        if x == "X":
            if c < len(y)-3 and y[c+1:c+4] == "MAS":
                counter += 1
                print("megvan")
            #print(y[c-4:c-1])
            if c > 2 and y[c-3:c] == "SAM":
                counter += 1
                print("megvan2")
            print(data[r][c])
            if r < len(data)-3 and data[r+1][c] == "M" and data[r+2][c] == "A" and data[r+3][c] == "S":
                counter += 1
                print("megvan3")
            if r > 2 and data[r-1][c] == "M" and data[r-2][c] == "A" and data[r-3][c] == "S" :
                counter += 1
                print("megvan4")
            if r < len(data)-3 and c < len(y)-3 and data[r+1][c+1] == "M" and data[r+2][c+2] == "A" and data[r+3][c+3] == "S":
                counter += 1
                print("megvan5")
            if r > 2 and c > 2 and data[r-1][c-1] == "M" and data[r-2][c-2] == "A" and data[r-3][c-3] == "S" :
                counter += 1
                print("megvan6")
            if r < len(data)-3 and c > 2 and data[r+1][c-1] == "M" and data[r+2][c-2] == "A" and data[r+3][c-3] == "S":
                counter += 1
                print("megvan7")
            if r > 2 and c < len(y)-3 and data[r-1][c+1] == "M" and data[r-2][c+2] == "A" and data[r-3][c+3] == "S" :
                counter += 1
                print("megvan8")
            
print(counter)

counter = 0
for r,y in enumerate(data):
    print(y)
    for c,x in enumerate(y):
        print(r, c)
        if x == "A" and c < len(y)-1 and r < len(data)-1 and c > 0 and r > 0:
            if ((data[r+1][c-1] == "M" and data[r-1][c+1] == "S") or (data[r+1][c-1] == "S" and data[r-1][c+1] == "M")) and \
                    ((data[r+1][c+1] == "M" and data[r-1][c-1] == "S") or (data[r+1][c+1] == "S" and data[r-1][c-1] == "M")):
                counter += 1
                print("megvan7")
print(counter)
