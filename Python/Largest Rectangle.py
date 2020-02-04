def largestRectangle(h):
    stack = []
    max_area = 0
    h.append(0)
    for i, n in enumerate(h):
        if len(stack) == 0 or n > stack[-1][1]:
            stack.append([i, n])
        elif n < stack[-1][1]:
            while len(stack) > 0 and n < stack[-1][1]:
                last = stack.pop()
                max_area = max(last[1] * (i - last[0]), max_area)
            stack.append([last[0], n])
    return max_area
