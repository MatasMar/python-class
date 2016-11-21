#!/usr/bin/env python3 -tt
import csv
import string

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
       triangle_numbers = [round(i * (i + 1) / 2) for i in range(100)]
       y = len(results)
       counter = 0
       triangle_word_count = 0
       while counter != y:
           word_ord_value = sum([ ord(i) - 96 for i in ''.join(results[counter]) if ord(i) - 96 > 0])
           word_with_uppercase = [ i for i in ''.join(results[counter]) if ord(i) - 96 < 0]
           if len(word_with_uppercase) != 0:
               final_value = word_ord_value - sum([ord (i) - 96 for i in word_with_uppercase])
           else:
               final_value = word_ord_value
           if final_value in triangle_numbers:
               triangle_word_count += 1
           counter += 1
       print (triangle_word_count)

def pascal():
    pascal_triangle_line = [1, 5, 10, 10, 5, 1] #nezinau ar reikejo input padaryt, ar ne
    next_line = [1, 5, 10, 10, 5, 1]
    lenght_of_new_line = len(pascal_triangle_line) + 1
    y = 1
    while y + 1 < lenght_of_new_line:
        next_line[y] = pascal_triangle_line[y - 1] + pascal_triangle_line[y]
        y += 1
    next_line.append(1)




def comprehensions():
    print([i * 2 + 1 for i in [0, 1, 2, 3]])
    print ([i % 3 == 0 for i in [3, 5, 9, 8]])
    print ([ i[3:] for i in ["TA_sam", "TA_guido", "student_poohbear", "student_htiek"] if len(i) <= 8])
    print ([i[:1].upper() for i in ['apple', 'orange', 'pear']])
    print ([i for i in ['apple', 'orange', 'pear'] if len(i) < 6])
    print ([[i, len(i)] for i in ['apple', 'orange', 'pear']]) # cia neisejo paprastu brackets padaryt
    print ({v:k for v in ['apple', 'orange', 'pear'] for k in [len(v)]}) # cia maiso tvarka kiekviena karta


def is_cyclone_word(word):
    word = [i for i in word.lower()]
    lenght_of_word = len(word) - 1
    character_counter = 0
    cycle_counter_for_reverse = 1
    character_counter_for_reverse = 0
    reverse = word[::-1]
    while character_counter <= lenght_of_word / 2:
        if ord(word[character_counter]) - 96 > ord(word[lenght_of_word - character_counter]) - 96:
            return False
        character_counter += 1
    while cycle_counter_for_reverse <= lenght_of_word / 2:
        if ord(reverse[character_counter_for_reverse]) - 96 > ord(reverse[lenght_of_word - cycle_counter_for_reverse]) - 96:
            return False
        cycle_counter_for_reverse += 1
        character_counter_for_reverse += 1
    return True

def  is_cyclone_phrase(phrase):
    phrase = phrase.split()
    cyclone_words = []
    for i in phrase:
        if is_cyclone_word(i) == True:
                cyclone_words.append(1)
    if len(phrase) == len(cyclone_words):
        print ('phrase is cyclone!')
    else:
        print ('phrase is not cyclone!')



if __name__ == "__main__":
    #gcd()
    #reverseDictionary()
    #triangleWords()
    #pascal()
    #comprehensions()
    is_cyclone_phrase(input('phrase:'))
    #is_cyclone_word(input('word:'))
