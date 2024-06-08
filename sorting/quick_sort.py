from common import *
import random



# time complexity: best: nlogn, worst n**2 (always pick largest/smallest as pivot)
# space complexity: best logn, worst n (stack space)
# not stable
def quick_sort(arr):
    quick_sort_helper(arr,0, len(arr))
    return arr
     




def quick_sort_helper(arr, l, r):
    if r-l <= 1:
        return
    
    pivot_idx = random.randint(l, r-1)
    pivot_value = arr[pivot_idx]
    swap(arr, pivot_idx, r-1)
    
    lp = l
    for rp in range(l, r):
        if arr[rp] < pivot_value:
            swap(arr, lp, rp)
            lp += 1

    swap(arr, lp, r-1)          # swap pivot back

    quick_sort_helper(arr, l, lp)     
    quick_sort_helper(arr, lp+1, r)


test_sorting(quick_sort)

