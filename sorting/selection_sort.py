from common import test_sorting, swap


# time complexity: best case O(n**2), worst case O(n**2)
# space complexity: O(1) given in place sorting
# unstable sorting caused by swapping. for example [4, 3, 4, 1] the first 4 will be swapped to the end

def selection_sort(arr):
    for l in range(len(arr)-1):
        min_idx = l
        for r in range(l+1, len(arr)):
            if arr[r] < arr[min_idx]:
                min_idx = r 
        swap(arr, l, min_idx)
    return arr 
        

test_sorting(selection_sort)

