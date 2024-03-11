#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [n for n  in num_list if (n%2==0) == True]
    return even_numbers

def make_exclamation(sentence_list):
    add_exclamations = [s + "!" for s in sentence_list]
    return add_exclamations


# squared_minus_one = [(n**2) - 1 for n in range(1,11)]

# print(squared_minus_one)

# filtered_list = [n for n in squared_minus_one if (n%3==0)== True]

# print(filtered_list)

# one_to_three = range(1,4)

# print(one_to_three)
