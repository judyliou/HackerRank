import sys
import os
from collections import deque
sys.setrecursionlimit(1500)

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.depth = 1

class Tree:
    def __init__(self):
        self.root = Node(1)
    
    def create_tree(self, data):
        queue = deque([self.root])
        data.reverse()
        while queue:
            node = queue.popleft()
            left, right = data.pop()
            if left != -1:
                node.left = Node(left)
                node.left.depth = node.depth + 1
                queue.append(node.left)
            if right != -1:
                node.right = Node(right)
                node.right.depth = node.depth + 1
                queue.append(node.right)
    
    def swap(self, k):
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node.depth % k == 0:
                node.left, node.right = node.right, node.left
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
    
    def in_order_traverse(self, node, result):
        if node:
            self.in_order_traverse(node.left, result)
            result.append(str(node.data))
            self.in_order_traverse(node.right, result)
        return result
        
def swapNodes(indexes, queries):
    tree = Tree()
    tree.create_tree(indexes)
    result = []
    for k in queries:
        tree.swap(k)
        result.append(tree.in_order_traverse(tree.root, []))
    return result
