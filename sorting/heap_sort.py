from common import *


def heapify(arr, idx):
    if idx >= len(arr):
        return 
    heapify(arr, 2*idx+1)
    heapify(arr, 2*idx+2)
    push_down(arr, idx)


def push_down(arr, idx):
    while idx < len(arr):
        # has both left and right child
        if 2*idx+2 < len(arr):
            root, left, right = arr[idx], arr[2*idx+1], arr[2*idx+2]
            if root <= left and root <= right:
                return 
            elif left <= root and left <= right:
                swap(arr, idx, 2*idx+1)
                idx = 2*idx+1
            else:
                swap(arr, idx, 2*idx+2)
                idx = 2*idx+2
        # has only left child
        elif 2*idx+1 < len(arr) and arr[2*idx+1] < arr[idx]:
            swap(arr, idx, 2*idx+1)
            idx = 2*idx+1
        else:
            return


def bubble_up(arr, idx):
    while idx > 0 and arr[(idx-1)//2] <= arr[idx]:
        swap(arr, idx, (idx-1)//2)
        idx = (idx-1)//2


class Heap():

    def __init__(self, arr):
        self.pq = arr 
        heapify(self.pq, 0)
        
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




def heap_sort(arr):
    heap = Heap(arr)
    res = []
    while not heap.is_empty():
        res.append(heap.pop())
    return res 

test_sorting(heap_sort)




            
    