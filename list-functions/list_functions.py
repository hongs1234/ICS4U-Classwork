from typing import List

def insert_at(original: List,
                value: int, 
                target_index: int) -> List:
    
    new = [0] * (len(original) + 1)

# copy up to target index
    i = 0
    while i < target_index:
        new[i] = original[i]
        i += 1

# insert
    new[i] = value
    i += 1

# copy from target to the end
    while i < len(new):
        new[i] = original[i-1]
        i += 1

    return new

def insert_sorted(original: List, value: int) -> List:
    i = 0
    while i < len(original):
        if original[i] > value:
            break
        i += 1
    
    return insert_at(original, value 1)