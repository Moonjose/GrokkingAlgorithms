# Recursion
# Not classic algorithms, just recursion practice.

from data import UNSORTED_LIST

def sum_recursive(arr):
    if len(arr) <= 0:
        return 0
    else:
        first = arr.pop(0)
        return first + sum_recursive(arr)

def count_recursive(arr):
    if not arr:
        return 0
    else:
        arr.pop()
        return 1 + count_recursive(arr)

def max_value_recursive(arr, max):
    if not arr:
        return max
    if arr[0] > max:
        max = arr[0]
    return max_value_recursive(arr[1:], max)

def find_max_value(arr):
    start_value = arr[0]
    return max_value_recursive(arr, start_value)

print(sum_recursive(UNSORTED_LIST.copy()))
print(count_recursive(UNSORTED_LIST.copy()))
print(find_max_value(UNSORTED_LIST.copy()))
