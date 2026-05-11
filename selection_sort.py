def selection_sort(arr) :
    for i in range(len(arr)) :
        index_of_min = i
        for j in range(i+1 , len(arr)):
            if arr[index_of_min] > arr[j]:
                index_of_min = j 
        arr[i] , arr[index_of_min] = arr[index_of_min] , arr[i]
    return arr