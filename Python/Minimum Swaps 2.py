def minimumSwaps(arr):
    swap = 0
    for i in range(len(arr)):
        while arr[i] != i+1:
            temp = arr[arr[i]-1]
            arr[arr[i]-1] = arr[i]
            arr[i] = temp
            swap += 1
            
    return swap
