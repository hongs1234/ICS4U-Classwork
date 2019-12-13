from typing import List

# 1
def has_repeat(word: str):
    if len(word) == 1:
        return False
    a = word[0]
    b = word[1]
    if a == b:
        return True
    return has_repeat(word[1:])


def sum_seven(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    if nums[0] == 7:
        return 7 + sum_seven(nums[1:])
    return sum_seven(nums[1:])


def ho_santa(word: str):
    if len(word) == 0:
        return ""
    if word[:2] == "ho":
        return "$" + ho_santa(word[2:])
    return word[0] + ho_santa(word[1:])