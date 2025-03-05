# import pytest

from defput import (
    is_string,
    reverse_string,
    is_palindrome,
    count_vowels,
    remove_first_occurrence,
)

def test_is_string():
    assert is_string("") == True
    assert is_string("abc") == False
    assert is_string("123") == False

def test_reverse_string():
    assert reverse_string("abc") == "cba"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("123") == "321"

def test_is_palindrome():
    assert is_palindrome("мадам") == True
    assert is_palindrome("Race car") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("Тропа налево повела на порт") == True

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("оловянный") == 4
    assert count_vowels("стринг") == 2

def test_remove_first_occurrence():
    assert remove_first_occurrence("hello") == "helo"
    assert remove_first_occurrence("banana") == "ban"
    assert remove_first_occurrence("aabbcc") == "abc"
