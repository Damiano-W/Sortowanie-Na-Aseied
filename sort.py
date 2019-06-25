from numpy.random import permutation as perm
from numpy import zeros
from numpy import sort
from random import randint
from time import perf_counter as time

array_size = 5000


def bombelki(to_be_sorted):
    # sorted_arr = zeros(array_size)
    sth_changed = True
    counter = 0
    while(sth_changed and counter<5000):
        counter+=1
        sth_changed = False
        for i in range(array_size - counter):
            idx = array_size - i - 1
            
            if to_be_sorted[idx]<to_be_sorted[idx - 1]:
                swap = to_be_sorted[idx]
                to_be_sorted[idx] = to_be_sorted[idx - 1]
                # sorted_arr[i]=to_be_sorted[i]
                to_be_sorted[idx - 1] = swap
                sth_changed = True
    # print(counter)
    # print(to_be_sorted-sort(to_be_sorted))
    return to_be_sorted
def select(to_be_sorted):
    for j in range(array_size):
        smallest=999999999
        smallest_idx = 0
        for i in range(array_size - j):
            idx = i + j
            if to_be_sorted[idx]<smallest:
                smallest = to_be_sorted[idx]
                smallest_idx = idx
        swap = to_be_sorted[j]
        to_be_sorted[j] = to_be_sorted[smallest_idx]
        to_be_sorted[smallest_idx]=swap
    return to_be_sorted


def qsort(arr, l=0, r=None):
    if r is None: r = len(arr) - 1
    i, j = l, r
    pivot = arr[(l + r) // 2]
    while i <= j:
        while arr[i] < pivot: i += 1
        while arr[j] > pivot: j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1; j -= 1
    if l < j: qsort(arr, l, j) 
    if r > i: qsort(arr, i, r)


myarr = perm(array_size)
arr = myarr
b_start = time()
bubble = bombelki(arr)
b_time = time() - b_start
print("bombelek:\t",b_time)
# print(rand_arr)
arr = myarr
s_start = time()
selection = select(arr)
s_time = time() - s_start
print("selection:\t", s_time)
# print(selection-sort(rand_arr))
arr = myarr
# print(arr)
q_start = time()
qsort(arr)
q_time = time() - q_start
print("QUICKSORT!:\t" ,q_time)
# print(arr-sort(myarr))

