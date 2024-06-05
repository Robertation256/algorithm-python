import random


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def is_sorted(arr):
    return sorted(arr) == arr


def gen_random_arr(size):
    return [random.randint(0, size) for i in range(size)]


def test_sorting(sort_algo):
    arr = gen_random_arr(100000)
    if sorted(arr) == sort_algo(arr):
        print(str(sort_algo) + " check passed.")
    else:
        print(str(sort_algo) + " check failed.")