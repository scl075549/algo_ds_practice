"""
Perform a binary search on a given input array
PARAMS:
    arr: int array, sorted, each element unique
    val: int value

Return the index of the value if found in the array
Return -1 if not found"""

def binary_search(arr, val):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if val == arr[mid]:
            return mid
        elif val < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# Test
input_array = [1, 3, 5, 7, 8, 9, 23, 44, 91]
# 1
print(binary_search(input_array, 3))
# -1
print(binary_search(input_array, 92))
