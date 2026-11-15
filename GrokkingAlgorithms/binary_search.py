# Binary Search Algorithm
# O(log n)  =>  worst and average case
# O(1)      =>  Best case

from data import SORTED_LIST

def binary_search(item, arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if (guess == item):
            return mid
        elif (guess < item):
            low = mid + 1
        else:
            high = mid - 1
    return None

print(binary_search(827, SORTED_LIST))
