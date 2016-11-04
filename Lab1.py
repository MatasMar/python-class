#!/usr/bin/env python3 -tt
from __future__ import division

def hello():
    print ('betkas')

def tictactoe():
    row  = ' |'.join([' '] * 3) + '\n'
    column = ('-' * 8 + '\n')
    print (row, row, row, sep = column)

def supertictactoe():
    row1 = ' |'.join([' '] * 3)
    column1 = ('+'.join(["--"] * 3))
    row2 = ' H'.join([row1] * 3) + '\n'
    column2 = 'H'.join([column1] * 3) + "\n"
    column3 = '+'.join(["=" * 8] * 3) + "\n"
    row3 =  ' H'.join([row1] * 3)
    column3 = column3.rstrip()
    print(row2, row2, row3, sep = column2)
    print (column3)
    print(row2, row2, row3, sep = column2)
    print (column3)
    print(row2, row2, row3, sep = column2)

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

def temperature():
    userInput = int(input('temperature F?'))
    tFahrenheit = (userInput - 32) / 1.8
    if tFahrenheit != round(tFahrenheit):
        print ("It is", round(tFahrenheit, 2), 'degrees Celsius')
    else:
        print ("It is", round(tFahrenheit), 'degrees Celsius')


if __name__ == "__main__":
    #hello()
    #tictactoe()
    supertictactoe()
    #fizz()
    #collatz()
    #temperature()
