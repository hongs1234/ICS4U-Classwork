

def test_binary_insert():
    original = [1, 3, 5]
    expected = [1, 3, 5, 6]
    assert binary_insert(original, 6) == expected

    original = [1, 3, 5]
    expected = [1, 3, 4, 5]
    assert binary_insert(original, 4) == expected

    original = [1, 3, 5]
    expected = [1, 3, 3, 5]
    assert binary_insert(original, 3) == expected

    original = [1, 3, 5]
    expected = [1, 2, 3, 5]
    assert binary_insert(original, 2) == expected