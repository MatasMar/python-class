#!/usr/bin/env python3 -tt

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
    dictionary = {}
    values = []
    newValue = 'y'
    while newValue == 'y':
        newValue = input('do you want to create a new dictionary value? (y for yes):')
        if newValue == 'y':
            userInput = input('dictionary item: ')
            userinputValue = input('item value: ').split()
            dictionary[userInput] = userinputValue
            values.append(userInput)
    print (values[0])
    print (dictionary)
    x = len(values)
    y = 1
    while y <= len(values):
        dictionary[''.join(dictionary.get(values[len(values) - x]))] = values[len(values) - x]
        del dictionary[values[len(values) - x]]
        x += 1
        y += 1
    print (dictionary)



if __name__ == "__main__":
    gcd()
    #reverseDictionary()
