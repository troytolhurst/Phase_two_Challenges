import pytest
from lib.grammar import *

#test for blank string, should return error message "No string"

def test_blank_string():
    with pytest.raises(ValueError) as e:
        grammar(" ")
    message = str(e.value)
    assert message == "No string"  

#test if return True when first character capital and last character suitable punctuation

def test_correct_grammar():
    result = grammar("Test string.")
    assert result == 'Grammar is correct!'

#test if return False when grammar incorrect

def test_all_incorrect_grammar():
    result = grammar("test string")
    assert result == 'String does not start with capital letter or end with suitable punctuation.'

def test_cap_no_punc():
    result = grammar("Test string")
    assert result == 'String does not end with suitable punctuation.'

def test_punc_no_cap():
    result = grammar("test string.")
    assert result == 'String does not start with capital letter'