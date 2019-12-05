from typing import List
import random


def bubble_sort(numbers: List[int]) -> List[int]:
    # optimization 1: if gone through without swapping, its sorted, stop looping
    # optimization 2: each pass, the last element is always sorted, don't loop to it anymore.
  
    # loop through len(numbers) times
        # loop through and compare two elements at a time
            # if the two elements are out of order, swap them
    
    if len(numbers) == 1:
        return numbers

    times_looped = 0
    is_sorted = False

    while is_sorted is False:
        is_sorted = True

        for n in range(len(numbers) - 1 - times_looped):
            a = numbers[n]
            b = numbers[n+1]
            if a > b:
                numbers[n] = b
                numbers[n+1] = a
                is_sorted = False
        times_looped += 1

    # return the sorted list
    return numbers


print(bubble_sort([1, 2, 3, 4, 5]))
print(bubble_sort([5, 4, 3, 2, 1, 0]))
print(bubble_sort([random.randrange(100) for _ in range(10)]))