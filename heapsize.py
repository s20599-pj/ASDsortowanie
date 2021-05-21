import time

def max_heapify(a, idd, heaps):
    left = 2 * idd + 1  # lewa strona drzewa
    right = 2 * idd + 2  # Prawa strona indexu
    if left < heaps and a[idd] < a[left]:
        largest = left
    else:
        largest = idd
    if right < heaps and a[largest] < a[right]:
        largest = right
    if idd != largest:
        a[largest], a[idd] = a[idd], a[largest]
        max_heapify(a, largest, heaps)

def build_max_heap(ar, heapsizer):
    for ix in range(int(heapsizer/2), -1, -1):
        max_heapify(ar, ix, heapsizer-1)

def heapsort(a, heapsiz):
    start = time.perf_counter()
    build_max_heap(a, heapsiz)
    for x in range(int(heapsiz), 0, -1):
        a[0], a[x-1] = a[x-1], a[0]
        heapsiz = heapsiz - 1
        max_heapify(a, 0, heapsiz)
    print("heapsize time: %ss" % (time.perf_counter() - start))
    with open('sorted.csv', 'w') as f:
        for item in a:
            f.write("%s\n" % item)
