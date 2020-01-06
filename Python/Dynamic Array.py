def dynamicArray(n, queries):
    # Write your code here
    result = []
    array = [[] for i in range(n)]
    ans = 0
    for i in queries:
        q, x, y = i[0], i[1], i[2]
        idx = (x ^ ans) % n
        seq = array[idx]
        if q == 1:
            seq.append(y)
        else:
            ans = seq[y% len(seq)]
            result.append(ans)
    return result
