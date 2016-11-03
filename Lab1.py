#!/usr/bin/env python3 -tt
def hello():
    print ('betkas')

def tictactoe():
    row  = ' |'.join([' ']*3)
    collumn = ('-'*8)
    print (row)
    print (collumn)
    print (row)
    print (collumn)
    print (row) # neveike sep komanda kazkodel

if __name__ == "__main__":
    hello()
    tictactoe()
