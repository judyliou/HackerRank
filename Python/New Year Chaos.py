def minimumBribes(q):
    sum = 0
    for i in range(len(q)):
        dis = q[i] - (i+1)
        if dis > 2:
            return 'Too chaotic'
        else:
            for j in range(max(0, q[i]-2), i):
                if q[j] > q[i]:
                    sum += 1
    return sum
