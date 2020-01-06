def leftRotate(n, d, a):
    left = a[d:]
    right = a[:d]
    return left + right
