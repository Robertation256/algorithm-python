from common import *


# time complexity: O(N + k)
# space complexity: O(k) where k is max_val - min_val + 1
# good to use if
# 0. this input is an array of intergers (cannot do floating points)
# 1. the input is always within a relatively small&fixed range
def count_sort(arr):
    mini, maxi = min(arr), max(arr)
    count = [0 for _ in range(maxi - mini + 1)]

    for n in arr:
        count[n-mini] += 1

    idx = 0
    for k in range(len(count)):
        for _ in range(count[k]):
            arr[idx] = mini + k
            idx += 1
    return arr 

test_sorting(count_sort)