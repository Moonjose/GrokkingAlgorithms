# Recursion
# Not classic algorithms, just recursion practice.

my_list = [-169, 470, -346, -96, 166, -451, -426, 340, 48, -404, -126, 96, -441, 431,
           19, -281, -462, -412, -56, -72, -429, -254, -408, 64, -66, -440, 346, 79,
           -374, 470, -272, 145, 142, 96, 470, -437, 90, 99, -94, -450, 499, -274,
           -453, 70, 379, -364, -204, -71, -353, 53, -380, 84, -185, 73, 335, 198,
           -315, -395, 95, 84, 154, -308, -119, -401, 60, 229, -436, 77, -439, 133,
           -290, 8, 196, 44, -63, 295, -179, -24, 99, 445]

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

print(sum_recursive(my_list.copy()))
print(count_recursive(my_list.copy()))
print(find_max_value(my_list.copy()))

