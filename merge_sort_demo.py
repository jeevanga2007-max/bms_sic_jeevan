import sys
import merge_sort as my

input_list = [int(i) for i in sys.argv[1:]]

print(my.divide_array(input_list, 0, len(input_list)-1))