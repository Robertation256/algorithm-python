from common import test_sorting, swap 


# time complexity: best case O(n) worst case O(n**2)
# space complexity: O(1) since in place
# stable sorting

def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] >= arr[j-1]:
                break 
            swap(arr, j, j-1)
    return arr

test_sorting(insertion_sort)

        