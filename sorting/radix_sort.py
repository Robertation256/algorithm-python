from common import *

# can be applied to data that can be lexicographically sorted
# time complexity O(nd) where d is the number of digits in the longest element
# space complexity O(n)
# stable sorting
def radix_sort(arr, radix = 10):
    max_val = max(arr)
    nex = [0 for _ in arr]
    exp = 0
    
    while max_val > 0:
        count = [0 for _ in range(radix)]
        d = radix ** exp
        for n in arr:
            count[(n//d)%radix] += 1

        for i in range(1, radix):
            count[i] += count[i-1]

        for i in range(len(arr)-1, -1, -1):  # go from the back to ensure sorting stability
            value = arr[i]
            digit = (value//d) % radix
            nex[count[digit]-1] = value
            count[digit] -= 1
        
        prev = arr
        arr = nex 
        nex = prev

        exp += 1
        max_val = max_val // radix 
    return arr 


test_sorting(radix_sort)

        



