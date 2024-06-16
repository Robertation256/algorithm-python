from typing import Callable

# reserve a tree array of size 2 * N for an input array of size N
# note that cell at index 0 is not used for the simplicity of parent/child/leave node index calculation
# merge function can be any binary associative function
# can thus segment tree can be used for range sum/min/max queries
# query complexity: logn
# update complexity: logn

class SegmentTree():

    def __init__(self, arr: list[int], merge_func: Callable[[int, int], int]):
        self.tree = [0 for _ in arr] + arr     # initialized tree to size 2 * N
        self.n = len(arr)
        self.merge_func = merge_func

        # build tree by merging in a botton-up fashion
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.merge_func(self.tree[2*i], self.tree[2*i+1])


    def update(self, idx, new_val):
        idx += self.n
        
        # update leaf node
        self.tree[idx] = new_val

        while idx > 1:
            idx //= 2  #shift to parent idx
            # merge left and right child
            self.tree[idx] = self.merge_func(self.tree[2*idx], self.tree[2*idx+1])


    def query(self, lb, rb):    # range query for [lb, rb)

        # shift to corresponding leaf node idx
        lb += self.n
        rb += self.n 

        res = None  # note that we assume merge_func(None, x) = x

        while lb < rb:
            # if left boundary is odd then left idx is a right child and it parent node is not fully contained in range
            # need to merge it now
            if lb & 1:    
                res = self.merge_func(self.tree[lb], res)
                lb += 1

            # if right boundary is odd then right most idx is a left child (rb is not inclusive) and it parent node is not fully contained in range
            # need to merge it now
            if rb & 1:
                rb -= 1
                res = self.merge_func(self.tree[rb], res)  

            # shift one level up
            lb //= 2
            rb //= 2
        
        return res

    


def min_func(a, b):
    if a is None:
        return b 
    if b is None:
        return a 
    return min(a, b)


st = SegmentTree([1, 5, 3, 7, 5], min_func)
print(st.query(0, 3))
print(st.query(1, 3))
print(st.query(1, 2))

st.update(0,3)
st.update(2,4)

print()
print(st.query(0, 3))
print(st.query(1, 3))
print(st.query(1, 2))