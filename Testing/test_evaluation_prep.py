import evaluation_prep as ep


def test_sum():
    assert ep.sum(1, 6) == 7
    assert ep.sum(-12, -4) == -16


def test_the_sum_of_list():
    assert ep.sum_of_list([3, 1, 4]) == 8
    assert ep.sum_of_list([-3, -1, 0]) == -4


def test_dictionary_of_words():
    words = ["hello", "hello", "bye"]
    expected = {"hello": 2, "bye": 1}
    result = ep.dictionary_of_words(words)
    assert result == expected

    words = ["a", "b", "b", "a", "c", "b"]
    expected = {"a": 2, "b": 3, "c": 1}
    result = ep.dictionary_of_words(words)
    assert result == expected
