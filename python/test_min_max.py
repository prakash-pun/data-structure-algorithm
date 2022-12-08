import string
DICTIONARY = 'dictionary.txt'

letter_scores = {
                    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 
                    'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 
                    'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 
                    'y': 4, 'z': 10
                }

def get_scrabble_dictionary():
    with open(DICTIONARY, 'rt', encoding='utf-8') as file:
        content = file.read().splitlines()
    return content

def score_word(word):
    """Return the score for a word using letter_scores.
    If the word isn't in DICTIONARY, it gets a score of 0.""" 
    dictionary = set(get_scrabble_dictionary())
    if word.upper() in dictionary:
        return sum(letter_scores.get(char.lower(), 0) for char in word)
    return 0

def remove_punctuation(word):
    """Helper function to remove punctuation from word"""
    table = str.maketrans({char:None for char in word if char in string.punctuation})
    return word.translate(table)

def get_word_largest_score(sentence):
    """Given a sentence, return the word with the largest score."""
    return max([remove_punctuation(word) for word in sentence.split()], key=score_word)


# from min_max_challenge import letter_scores, get_scrabble_dictionary, score_word, get_word_largest_score

def test_words_uppercase():
    assert score_word('ABANDON') == 10
    assert score_word('VOID') == 8

def test_words_lowercase():
    assert score_word('biodiversity') == 21
    assert score_word('entrepreneurs') == 15

def test_madeup_words():
    assert score_word('sheeps') == 0
    assert score_word('xylophenatic') == 0

def test_word_largest_score():
    assert get_word_largest_score("Beautiful is better than ugly.") == 'Beautiful'
    assert get_word_largest_score("Explicit is better than implicit.") == 'Explicit'

def test_word_with_punctuation():
    assert get_word_largest_score('In the face of ambiguity, refuse the temptation to guess.') == 'ambiguity'
    assert get_word_largest_score('Errors should never pass silently.') == 'silently'

def test_madeup_sentence():
    # All of the words have a score of 0, return the first word
    assert get_word_largest_score('wefpie fefq fqpw pwqww') == 'wefpie'
    assert get_word_largest_score('pwqw zxxz lmpny zsxrwq') == 'pwqw'