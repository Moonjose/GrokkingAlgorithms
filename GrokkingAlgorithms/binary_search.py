# Binary Search Algorithm
# O(log n)  =>  worse and average case
# O(1)      =>  Best case

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

my_list = [
    3, 11, 19, 27, 34, 46, 52, 61, 70, 78,
    85, 93, 104, 112, 118, 127, 139, 146, 151, 163,
    170, 178, 186, 195, 203, 214, 221, 229, 238, 244,
    256, 263, 271, 280, 288, 297, 305, 312, 324, 331,
    339, 347, 356, 362, 375, 381, 390, 398, 407, 415,
    423, 432, 441, 449, 458, 466, 473, 485, 492, 500,
    509, 517, 526, 534, 541, 553, 560, 568, 577, 586,
    594, 603, 611, 620, 628, 635, 647, 654, 662, 671,
    680, 688, 697, 705, 713, 722, 730, 739, 748, 756,
    765, 773, 781, 790, 802, 811, 827, 843, 866, 912,
]

print(binary_search(827, my_list))
