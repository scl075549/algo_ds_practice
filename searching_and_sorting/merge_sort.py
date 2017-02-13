"""
Merge Sort is a recursive algorithm that continually splits a list in half.
If the list is empty or has one item, it is sorted by definition (base case).
If the list has more than one item, we split the list and recursively invoke a merge sort on both halves.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    """Take two sorted lists and returns a single sorted list by comparing the elements one at a time:"""

    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])

arr = [54,26,93,17,77,31,44,55,20]
print(merge_sort(arr))
