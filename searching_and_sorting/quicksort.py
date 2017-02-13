"""Quicksort algorthm has two phases:
    - partition phase
    - sort phase

    Most of the work is done in the partition phase --> decides where to divide the work. The sort phase sorts the two smaller lists generated from the partition phase
"""
import random

# This implementation is not in-place but more concise:
def sort(array):
    less, equal, greater = [], [], []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        return sort(less) + equal + sort(greater)
    else:
        return array

arr = [12,4,5,6,7,3,1,15]
print(sort(arr))

# Quicksort w/o additional memory usage (in-place)
def quicksort(array):
    qsort(array, 0, len(array)-1)

def qsort(array, start, end):
    if end < start:
        return
    pivot = partition(array, start, end)
    qsort(array, start, pivot-1)
    qsort(array, pivot+1, end)

def partition(array, start, end):
    pivot_value = array[start]
    left, right = start+1, end

    while True:
        while left <= right and array[left] <= pivot_value:
            left += 1
        while right >= left and array[right] >= pivot_value:
            right -= 1
        if right < left:
            break
        else:
            array[left], array[right] = array[right], array[left]
    # swap pivot value into split point
    array[start], array[right] = array[right], array[start]
    return right

arr = [54,26,93,17,77,31,44,55,20]
quicksort(arr)
print(arr)
