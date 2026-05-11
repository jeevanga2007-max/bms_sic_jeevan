import partition_assignment
import sys

arr = []

for i in range(1, len(sys.argv)):
    arr.append(int(sys.argv[i]))

print(f'User given elements are \n', arr)
print(f'Partitioned array is \n', partition_assignment.partition(arr))