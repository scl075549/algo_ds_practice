"""
Bubble sort (or Sinking sort, depending on the direction you rearrange elements) is an elementary sorting algorithm. Imagine an array arranged vertically: With each successive pass through the array, the smallest element 'bubbles up' to the top, eventually leaving the sorted array in place. Conversely (and shown below), in a sinking sort, the largest element 'sinks' to the bottom (end) of the array with each iteration.
"""
def bubble_sort(arr):
    for n in range(len(arr)-1, 0, -1): # search 1 less each pass through
        for i in range(n):
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)

def swap(arr, x, y):
    tmp = arr[x]
    arr[x] = arr[y]
    arr[y] = tmp

# Unsorted array:
arr = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
print(arr)
# Expected : [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, ,9]
bubble_sort(arr)
print(arr)
