# Solution 1
def riddle(arr):
    cur = arr
    output = [max(arr)]
    for i in range(len(arr)-1):
        prev = cur
        cur = []
        for j in range(len(prev)-1):
            cur.append(min(prev[j], prev[j+1]))
        output.append(max(cur))
    return output
    
# Solution 2 
def riddle(arr):
    stack = []
    max_window = {}
    arr.append(0)
    
    # identify the largest window a number is the minimum for
    # 6, 3, 5, 1, 12 --> max_window = {6: 1, 5: 1, 3: 3, 12: 1, 1: 5}
    for i, n in enumerate(arr):
        if len(stack) == 0 or n > stack[-1][1]:
            stack.append([i, n])
        else:
            while len(stack) > 0 and n < stack[-1][1]:
                last = stack.pop()
                max_window[last[1]] = max((i - last[0]), max_window.get(last[1], -1))
            stack.append([last[0], n])

    # covert to the max value given the window size
    # inverted_windows = {1: 12, 3: 3, 5: 1}
    inverted_window = {}
    for k, v in max_window.items():
        inverted_window[v] = max(k, inverted_window.get(v, -1))

    # iterate through the window size ([12, -1, 3, -1, 1]) and fill missing values
    arr.pop()
    ans = []
    for i in range(1, len(arr)+1):
        ans.append(inverted_window.get(i, -1))
    for i in range(len(arr)-2, 0, -1):
        if ans[i] == -1 or ans[i] < ans[i+1]:
            ans[i] = ans[i+1]
    return ans
