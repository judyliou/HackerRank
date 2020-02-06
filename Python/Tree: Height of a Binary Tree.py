from collections import deque

def height(root):
    if root is None:
        return 0

    queue = deque([(root, 0)])
    while len(queue) != 0:
        cur = queue.popleft()
        node = cur[0]
        height = cur[1]
        if node.left != None:
            queue.append((node.left, height+1))
        if node.right != None:
            queue.append((node.right, height+1))
    return height
