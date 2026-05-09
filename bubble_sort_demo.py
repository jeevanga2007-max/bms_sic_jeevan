import bubble_sort
import sys

result_not_optimized = bubble_sort.bubble_sort(sys.argv[1:])
#result_optimized = bubble_sort.bubble_sort_optimized(sys.argv[1:])
print("Not optimized: ", result_not_optimized)
#print("Optimized: ", result_optimized)