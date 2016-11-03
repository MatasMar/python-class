#!/usr/bin/env python3 -tt
n = input ('number:')
hey = []
while n != 0:
    if n%5 == 0 or n%3 == 0:
        hey.append(n) 
    n = n-1
print (sum(hey))
