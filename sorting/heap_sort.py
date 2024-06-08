from common import *

#recursive approach takes up logn extra space
def heapify_recursive(arr, idx):
    if idx >= len(arr):
        return 
    heapify_recursive(arr, 2*idx+1)
    heapify_recursive(arr, 2*idx+2)
    push_down(arr, idx)


def heapify(arr):
    for i in range((len(arr)-1)//2, -1, -1):
        push_down(arr, i)



def push_down(arr, idx, limit = -1):
    limit = len(arr) if limit < 0 else limit 
    while idx < limit:
        largest_idx = idx

        if 2*idx + 1 < limit and arr[2*idx + 1] > arr[largest_idx]:
            largest_idx = 2*idx + 1
        if 2*idx + 2 < limit and arr[2*idx + 2] > arr[largest_idx]:
            largest_idx = 2 * idx + 2

        if largest_idx == idx:
            return

        swap(arr, idx, largest_idx)
        idx = largest_idx


def bubble_up(arr, idx):
    while idx > 0 and arr[(idx-1)//2] <= arr[idx]:
        swap(arr, idx, (idx-1)//2)
        idx = (idx-1)//2


class MaxHeap():

    def __init__(self, arr):
        self.pq = arr 
        heapify(self.pq)
        
    def push(self, elem):
        self.pq.append(elem)
        bubble_up(self.pq, len(self.pq)-1)

    def pop(self):
        swap(self.pq, 0, len(self.pq)-1)
        res = self.pq.pop()
        push_down(self.pq, 0)
        return res

    def is_empty(self):
        return len(self.pq) <= 0

    # sort by swapping heap top to end of priority queue and reduce push_down range
    def sort(self):
        for i in range(len(self.pq)-1, -1, -1):
            swap(self.pq, 0, i)
            push_down(self.pq, 0, i)
        return self.pq




def heap_sort(arr):
    #first heapify into a max heap then do swapping heap top to end of priority queue and reduce push_down range
    heap = MaxHeap(arr)
    return heap.sort()

test_sorting(heap_sort)




            
    