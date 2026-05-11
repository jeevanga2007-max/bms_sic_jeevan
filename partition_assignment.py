
def partition(arr):
    pivot = arr[-1]
    pos = 0
    for i in range(len(arr)-1):
        if arr[i] <= pivot:
            temp = arr[i]
            for j in range(i, pos, -1):
                arr[j] = arr[j-1]
            arr[pos] = temp
            pos += 1
    for j in range(len(arr)-1, pos, -1):
        arr[j] = arr[j-1]

    arr[pos] = pivot
    return arr

