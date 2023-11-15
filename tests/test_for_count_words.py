from lib.count_words import *

def test_for_empty_string_in_count_words():
    result = count_words(" ")
    assert result == 0

def test_for_one_word_in_count_words():
    result = count_words("one")
    assert result == 1

def test_for_three_words_in_count_words():
    result = count_words("one two three")
    assert result == 3


