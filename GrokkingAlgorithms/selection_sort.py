# Selection Sort Algorithm
# O(n²)  =>  worse, average and best case

def find_smallest(arr):
    smaller = arr[0]
    smaller_idx = 0

    for i in range(1, len(arr)):
        if arr[i] < smaller:
            smaller = arr[i]
            smaller_idx = i
    return smaller_idx

def selection_sort(arr):
    new_arr = []
    arr_cpy = list(arr)

    for _ in range(len(arr_cpy)):
        smaller = find_smallest(arr_cpy)
        new_arr.append(arr_cpy.pop(smaller))
    return new_arr

print(selection_sort([42, -7, 0, 999, 3, 3, -150, 88, 17, -7, 256, 1, 73, -1, 500, 12, 0, 64, -33, 8, 1024, 5, 42, -999, 21]))