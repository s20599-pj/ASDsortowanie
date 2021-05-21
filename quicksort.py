import time

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q + 1, r)

def partition(A, p, r):
    pivot = A[r]
    smaller = p
    for j in range(p, r):
        if A[j] <= pivot:
            A[smaller], A[j] = A[j], A[smaller]
            smaller = smaller + 1
    A[smaller], A[r] = A[r], A[smaller]
    return smaller

def quicksortWithCounter(A, p, r):
    start = time.perf_counter()
    quicksort(A, p, r)
    print("Quicksort time: %ss" % (time.perf_counter()-start))
    
