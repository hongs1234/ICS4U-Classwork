from typing import List


def binary_insert(nums: List[int], target: int):
    index = 0
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] > target:
            end = mid - 1
            index = mid
        elif nums[mid] <= target:
            start = mid + 1
            index = start
    
    nums.insert(index, target)
    return nums