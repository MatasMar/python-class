#!/usr/bin/env python3 -tt
import csv

def gcd():
    userInputA = int(input("number a:"))
    userInputB = int(input("number b:"))
    GCD = []
    divisor = userInputA
    while divisor != 0:
        if userInputA % divisor == 0 and userInputB % divisor == 0:
            GCD.append(divisor)
        divisor -= 1
    print ('greatest common divisor:', max(GCD))

def reverseDictionary():
    dictionary = {"CA": "US", "NY": "US", "ON": "CA"}
    inverse_dictionary = {}
    for key, value in dictionary.items():
        if value not in inverse_dictionary:
            inverse_dictionary[value] = []
        inverse_dictionary[value].append(key)
    print (inverse_dictionary)

def triangleWords():
   with open('words', newline= '') as inputfile:
       results = inputfile.read().split()
       resultsList = []
       miniResultsList = []
       x = len(results) - 6
       y = len(list(results[len(results) - x])) - 1
       print (ord(''.join(list(results[len(results) - x])[len(list(results[len(results) - x])) - y])))
       print (y)
       print (x)
       print (len(results))
       while y >= 0:
           miniResultsList.append(ord(''.join(list(results[len(results) - x])[len(list(results[len(results) - x])) - y])))
           y -= 1
       print (miniResultsList)

def pascal():
    pascal_triangle_line = [1, 5, 10, 10, 5, 1] #nezinau ar reikejo input padaryt, ar ne 
    next_line = [1, 5, 10, 10, 5, 1]
    lenght_of_new_line = len(pascal_triangle_line) + 1
    y = 1
    while y + 1 < lenght_of_new_line:
        next_line[y] = pascal_triangle_line[y - 1] + pascal_triangle_line[y]
        y += 1
    next_line.append(1)
    print (next_line)

if __name__ == "__main__":
    #gcd()
    #reverseDictionary()
    #triangleWords()
    pascal()
