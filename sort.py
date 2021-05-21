from heapsize import heapsort
from quicksort import quicksortWithCounter
from shellsort import shellSort
import csv
import sys
sys.setrecursionlimit(1000000000)

with open('random.csv', 'r') as f:
    randomArray = list(csv.reader(f))
with open('sorted.csv', 'r') as f:
    sortedArray = list(csv.reader(f))
with open('reverse.csv', 'r') as f:
    reversedArray = list(csv.reader(f))    

print("Random: ")
quicksortWithCounter(randomArray, 0, len(randomArray)-1)
shellSort(randomArray)
heapsort(randomArray, len(randomArray))

print("Sorted: ")
quicksortWithCounter(sortedArray, len(sortedArray)-1, len(sortedArray)-1)
shellSort(sortedArray)
heapsort(sortedArray, len(sortedArray))

print("Reversed: ")
quicksortWithCounter(reversedArray, 0, len(reversedArray)-1)
shellSort(reversedArray)
heapsort(reversedArray, len(reversedArray))