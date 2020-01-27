def maxSubsetSum(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return max(arr)
        
    arr[1] = max(arr[:2])
    for i in range(2, len(arr)):
        arr[i] = max(arr[i-2] + arr[i], arr[i-1], arr[i])
    return arr[-1]
