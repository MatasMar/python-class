#!/usr/bin/env python3 -tt
from __future__ import division
n = input ('number:')
hey = []
x = 0
y = n
while y > 0:
    while n != 1:
        if n/2 == int(n/2):
            n = n/2
            n = int(n)
        else:
             n = n*3+1
             n = int(n)
        x = x+1
    y = y-1
    n = y
    hey.append(x)
    x = 0
print (max(hey))
