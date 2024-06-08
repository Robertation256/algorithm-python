
from common import *
from math import floor


# runs in O(n) given a uniform distribution over its range
# worst case O(n**2) when all elements are placed in one bucket
# space complexity O(n)
# stable if the underlying sort is stable
def bucket_sort(arr):
    
    mini = min(arr)
    maxi = max(arr)

    buckets = [[] for i in range(len(arr)) ]

    for n in arr:
        idx =  max(floor((n - mini) / (maxi - mini) * n ), n-1)
        buckets[idx].append(n)
    
    res = []
    for b in buckets:
        b.sort()
        for e in b:
            res.append(e)
    return res

test_sorting(bucket_sort)

