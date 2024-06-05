from common import *


# time complexity: best case O(n) worst case O(n**2)
# space complexity: O(1) since in place
# stable sorting

def bubble_sort(arr):
    is_sorted = False
    while not is_sorted:
        is_sorted = True 
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)
                is_sorted = False 
    return arr 

test_sorting(bubble_sort)