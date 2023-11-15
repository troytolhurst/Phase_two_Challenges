from lib.make_snippet import *

def test_for_six_word_sentence():
    result = make_snippet("This string is really really long")
    assert result == "This string is really really..."

def test_for_one_word_sentence():
    result = make_snippet("one")
    assert result == "one"

def test_for_ten_word():
    result = make_snippet("one two three four five six seven eight nine 10")
    assert result == "one two three four five..."