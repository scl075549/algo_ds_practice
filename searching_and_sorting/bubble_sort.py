"""
Bubble sort is an elementary sorting algorithm. The idea is to imagine bubbling the smallest elements of a (vertical) array to the top; then bubble the next smallest; then so on until the entire array is sorted.
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
