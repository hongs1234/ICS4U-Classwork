from typing import List
import random

def merge_sort(numbers: List[int]) -> List[int]:
    # base case
    if len(numbers) == 1:
        return numbers

    # find the midpoint
    mid = len(numbers) // 2

    # two recursive steps
    # mergesort left
    left = merge_sort(numbers[:mid])

    # mergesort right
    right = merge_sort(numbers[mid:])

    # merge the two together


    # loop through both lists with two markers
    sorted_list = []
    left_marker = 0
    right_marker = 0
    while left_marker < len(left) and right_marker < len(right):
        if left[left_marker] < right[right_marker]:
            sorted_list.append(left[left_marker])
            left_marker += 1
        else:
            sorted_list.append(right[right_marker])
            right_marker += 1

    # if right value less than left value, add right value to sorted, increase right marker
    # if left value less than right value, add left value to sorted, increase left marker

    # create a while loop to gather the rest of the values from either list
    while right_marker < len(right):
        sorted_list.append(right[right_marker])
        right_marker += 1
    
    while left_marker < len(left):
        sorted_list.append(left[left_marker])
        left_marker += 1
 
    # return the sorted list
    return sorted_list



print(merge_sort([1, 2, 3, 4, 5]))
print(merge_sort([5, 4, 3, 2, 1, 0]))
print(merge_sort([random.randrange(100) for _ in range(10)]))