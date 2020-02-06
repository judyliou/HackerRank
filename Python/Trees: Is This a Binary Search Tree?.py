# can't just check left and right because the case that 
# (node.right.data > node.data) and (node.right.data > node.parent.data) should be detected
# --> using Min Max to set the feasible range 

def checkBST(root):
    return isBST(root, None, None)

def isBST(root, min, max):
    if root == None:
        return True
    if (min != None and root.data <= min) or (max != None and root.data >= max):
        return False
    return isBST(root.left, min, root.data) and isBST(root.right, root.data, max)
