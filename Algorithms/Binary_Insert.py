from typing import List


def binary_insert(nums: List[int], target: int):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if target == nums[mid]:
            nums.insert(mid, target)
            return nums
        elif target > nums[mid]:
            start = mid + 1
        elif target < nums[mid]:
            end = mid - 1
    
    if start > end:
        nums.insert(start, target)
        return nums
