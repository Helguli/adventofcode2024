#!/bin/env python

f = open("input02", "r")

def safe(l):
    prev = None
    inc = None
    for a in l:
        if not prev :
            prev = a
            continue
        if inc is None:
            inc = True if prev < a else False
        if not inc and prev <= a:
            return 0
        if inc and prev >= a:
            return 0
        if abs(a-prev) > 3:
            return 0
        prev = a
    return 1


def trySafe(l):
    prev = None
    inc = None
    for i,a in enumerate(l):
        if not prev :
            prev = a
            continue
        if inc is None:
            inc = True if prev < a else False
        if not inc and prev <= a:
            l1 = [i for i in l]
            del l1[i]
            if safe(l1):
                return 1
            if i != 0:
                l1 = [i for i in l]
                del l1[i-1]
                if safe(l1):
                    return 1
            if i != len(l)-1:
                l1 = [i for i in l]
                del l1[i+1]
                if safe(l1):
                    return 1
            return 0
        if inc and prev >= a:
            l1 = [i for i in l]
            del l1[i]
            if safe(l1):
                return 1
            if i != 0:
                l1 = [i for i in l]
                del l1[i-1]
                if safe(l1):
                    return 1
            if i != len(l)-1:
                l1 = [i for i in l]
                del l1[i+1]
                if safe(l1):
                    return 1
            return 0
        if abs(a-prev) > 3:
            l1 = [i for i in l]
            del l1[i]
            if safe(l1):
                return 1
            if i != 0:
                l1 = [i for i in l]
                del l1[i-1]
                if safe(l1):
                    return 1
            if i != len(l)-1:
                l1 = [i for i in l]
                del l1[i+1]
                if safe(l1):
                    return 1
            return 0
        prev = a
    return 1


safesum = 0
for x in f:
    y = x.split()
    z = [int(item) for item in y]
    safesum += trySafe(z)

print(safesum)
