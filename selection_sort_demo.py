import selection_sort
import sys

arr = list(int(x) for x in sys.argv[1:])

array_sorted = selection_sort.selection_sort(arr)

print("Sorted array:", array_sorted)