from list_functions import *

def test_insert_at():
    original = [1, 2, 3, 4]
    expecting = [1, 2, 5, 3, 4]
    result = insert_at(original, 5, 2)
    assert result == expecting

    original = [1, 2, 3, 4]
    expecting = [5, 1, 2, 3, 4]
    result = insert_at(original, 5, 0)
    assert result == expecting

    original = [1, 2, 3, 4]
    expecting = [1, 2, 3, 4, 5]
    result = insert_at(original, 5, 4)
    assert result == expecting

    original = [1]
    expecting = [1, 0, 5]
    result = insert_at(original, 5, 2)
    assert result == expecting


def test_insert_sorted():
    # test middle
    original = [1, 2, 3, 4]
    expecting = [1, 2, 2, 3, 4]
    result = insert_sorting(original, 2)
    assert result == expecting

    # test beginning
    original = [1, 2, 3, 4]
    expecting = [0, 1, 2, 3, 4]
    result = insert_sorted(original, 0)
    assert result == expecitng

    # test end
    original = [1, 2, 3, 4]
    expecting = [1, 2, 3, 4, 5]
    result = insert_sorted(original, 5)
    assert result == expecting