#!/usr/bin/env python3 -tt
from __future__ import division

def hello():
    print ('betkas')

def tictactoe():
    row  = ' |'.join([' '] * 3) + '\n'
    column = ('-' * 8 + '\n')
    print (row, row, row, sep = column)

def fizz():
    userInput = input ('number:')
    chain = []
    while userInput != 0:
        if userInput % 5 == 0 or userInput % 3 == 0:
            hey.append(userInput)
        userInput -= 1
    print (sum(chain))

def collatz():
    userInput = input ('number:')
    chain = []
    i = userInput
    x = 0
    while i > 0:
        while userInput != 1:
            if userInput / 2 == round(userInput / 2):
                userInput = userInput / 2
                userInput = round(userInput)
            else:
                userInput = userInput * 3 + 1
                userInput = round(userInput)
            x += 1
        i -= 1
        userInput = i
        chain.append(x)
        x = 0
    print (max(chain))

if __name__ == "__main__":
    #hello()
    tictactoe()
    #fizz()
    #collatz()
