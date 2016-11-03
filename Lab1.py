#!/usr/bin/env python3 -tt
from __future__ import division

def hello():
    print ('betkas')

def tictactoe():
    row  = ' |'.join([' '] * 3)
    collumn = ('-' * 8)
    print (row)
    print (collumn)
    print (row)
    print (collumn)
    print (row) # neveike sep komanda kazkodel

def fizz():
    n = input ('number:')
    hey = []
    while n != 0:
        if n % 5 == 0 or n % 3 == 0:
            hey.append(n)
        n = n - 1
    print (sum(hey))

def collatz():
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

if __name__ == "__main__":
    hello()
    tictactoe()
    fizz()
    collatz()
