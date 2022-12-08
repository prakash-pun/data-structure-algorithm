# A palindrome is a word, phrase, number or sequence of words that reads the same backwards as forward. Punctuation and spaces between the words or lettering is allowed.

import re

def remove_punctuation(words):
    '''Helper function to return a string, removing all punctuations and spaces'''
    return re.sub('\W+', '', words)

def is_palindrome(words):
    reversed_words = ''.join(reversed(words))
    return remove_punctuation(words.lower()) == remove_punctuation(reversed_words.lower())


print(is_palindrome("chalenge"))