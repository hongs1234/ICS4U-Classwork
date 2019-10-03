import evaluation_prep


def test_sum():
    assert evaluation_prep.sum(1, 6) == 7
    assert evaluation_prep.sum(-12, -4) == -16


def test_the_sum_of_list():
    assert evaluation_prep.sum_of_list([3, 1, 4]) == 8
    assert evaluation_prep.sum_of_list([-3, -1, 0]) == -4


def test_dictionary_of_words():
    assert evaluation_prep.dictionary_of_words(["hello", "hello"]) == {"hello": 2}
    assert evaluation_prep.dictionary_of_words(["hi", "hello", "hi", "bye"]) == {"hi": 2}
