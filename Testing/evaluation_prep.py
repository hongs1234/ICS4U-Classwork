# 3. Create a function that takes a list of words. 
# Then create and return a dictionary where the key is 
# the word and the value is how many times the word 
# appears in the list.

from typing import List


def sum(a: int, b: int) -> int:
    return a + b


def sum_of_list(numbers: List[int]) -> int:
    the_sum = 0
    for num in numbers:
        the_sum += num

    return the_sum


def dictionary_of_words(words: List[str]) -> dict:
    a = words[0]
    i = 0
    for word in words:
        if word == a:
            i += 1
    
    return {a: i}
