from algorithms_test import *

def test_has_repeat():
    assert has_repeat("aba") == False
    assert has_repeat("baa") == True
    assert has_repeat("aabcc") == True
    assert has_repeat("ababab") == False


def test_sum_seven():
    assert sum_seven([1, 2, 3, 4, 5, 6, 7]) == 7
    assert sum_seven([7, 7, 7, 1]) == 21
    assert sum_seven([1, 2, 3, 4]) == 0


def test_ho_santa():
    assert ho_santa("hollo, whorld!") == "$llo, w$rld!"
    assert ho_santa("have a holly-holly christmas") == "have a $lly-$lly christmas"
    assert ho_santa("holucia, hobarbara, hocruz") == "$lucia, $barbara, $cruz"
    assert ho_santa("hohoho!") == "$$$!"