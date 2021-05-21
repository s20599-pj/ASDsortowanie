import time

def shellSort(list):
    start = time.perf_counter()
    n = len(list)
    polowa = n // 2
    while polowa > 0:
        for i in range(polowa, n):
            temp = list[i]
            j = i
            while j >= polowa and list[j-polowa] > temp:
                list[j] = list[j-polowa]
                j -= polowa
            list[j] = temp
        polowa = polowa // 2
    print("Shellsort time: %ss" % (time.perf_counter()-start))
    