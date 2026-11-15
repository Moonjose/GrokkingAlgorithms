# Quicksort Algorithm
# O(n log n)  =>  Average and Best case
# O(n²)      =>  Worst case


from data import UNSORTED_LIST

def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort(UNSORTED_LIST))
