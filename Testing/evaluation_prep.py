from typing import List


def sum(a: int, b: int) -> int:
    """Add two integers

    Arg:
        a: an integer
        b: an integer
    Returns:
        The sum of two integers.
    """

    return a + b


def sum_of_list(numbers: List[int]) -> int:
    """Give the sum of a list

    Arg:
        numbers: A list of integers
    Returns:
        The sum of all the integers in numbers.
    """

    the_sum = 0
    for num in numbers:
        the_sum += num

    return the_sum


def dictionary_of_words(words: List[str]) -> dict:
    """Create a dictionary

    Arg:
        words: a list of words
    Returns:
        A dictionary with a word as the key and the
        number of times it appeared as the value.
    """

    occurances = {}
    for word in words:
        if word not in occurances.keys():
            occurances[word] = 1
        else:
            occurances[word] += 1

        # try:
        #     occurances[word] += 1
        # except KeyError:
        #     occurances[word] = 1

    return occurances
