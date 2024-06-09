from common import *


# time complexity O(nlogn)
# space complexity O(n) + O(logn)
def merge_sort(arr):
    if len(arr) < 2:
        return arr 
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    res = []
    lp, rp = 0, 0
    while lp < len(left) and rp < len(right):
        if left[lp] <= right[rp]:
            res.append(left[lp])
            lp += 1
        else:
            res.append(right[rp])
            rp += 1
    while lp < len(left):
        res.append(left[lp])
        lp += 1
    while rp < len(right):
        res.append(right[rp])
        rp += 1
    return res 


test_sorting(merge_sort)