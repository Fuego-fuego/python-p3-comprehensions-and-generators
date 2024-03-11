#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [n for n  in num_list if (n%2==0) == True]
    return even_numbers

def make_exclamation(sentence_list):
    add_exclamations = [s + "!" for s in sentence_list]
    return add_exclamations



