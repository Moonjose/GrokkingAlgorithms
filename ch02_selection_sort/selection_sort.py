# Selection Sort Algorithm
# O(n²)  =>  worst, average and best case

from data import SMALL_LIST

def find_smallest(arr):
    smallest = arr[0]
    smallest_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i
    return smallest_idx

def selection_sort(arr):
    new_arr = []
    arr_cpy = list(arr)

    for _ in range(len(arr)):
        smallest = find_smallest(arr_cpy)
        new_arr.append(arr_cpy.pop(smallest))
    return new_arr

print(selection_sort(SMALL_LIST))
