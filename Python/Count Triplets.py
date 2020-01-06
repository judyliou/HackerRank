def countTriplets(arr, r):
    right = {}
    left = {}
    cnt = 0
    for i in arr:
        if i in right:
            right[i] += 1
        else:
            right[i] = 1

    for s in range(len(arr)):
        j = arr[s]
        right[j] = right[j] - 1
        if j % r == 0:
            i = left.get(int(j/r), 0)
            k = right.get(j*r, 0)
            cnt += i * k
        left[j] = left.get(j, 0) + 1
    return cnt
