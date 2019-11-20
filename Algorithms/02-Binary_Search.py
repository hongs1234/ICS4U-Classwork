from typing import List

def binary_search(target: int, numbers: List[int]):
    start = 0
    end = len(numbers) - 1
    mid = (start + end) // 2

    while start <= end:
        if target > mid:
            start = mid + 1
        elif target < mid:
            end = mid -1
        elif target == mid:
            print("Target found")
            break
        else:
            print(f"Target not found. Number is between {mid-1} and {mid+1}")
            break



def test_empty_list():
    assert binary_search(5, []) == -1


def test_number_not_found():
    dataset = list(range(100))
    assert binary_search(100, dataset) == -1

    dataset = list(range(3))
    assert binary_search(100, dataset) == -1


def test_found_last_index():
    dataset = list(range(100))
    assert binary_search(99, dataset) == 99


def test_found_middle_index():
    dataset = list(range(3))
    assert binary_search(1, dataset) == 1

    dataset = list(range(100, 200))
    assert binary_search(134, dataset) == 34


def test_found_first_index():
    dataset = list(range(100))
    assert binary_search(0, dataset) == 0