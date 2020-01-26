def triplets(a, b, c):
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    c = sorted(list(set(c)))
    
    p1, p3 = 0, 0 
    cnt = 0
    for i in range(len(b)):
        while p1 < len(a):
            if a[p1] > b[i]: break    
            p1 += 1
        while p3 < len(c):
            if c[p3] > b[i]: break
            p3 += 1  
        cnt += p1 * p3        
    return cnt
