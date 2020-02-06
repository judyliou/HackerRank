def lca(root, v1, v2):
    v1, v2 = min(v1, v2), max(v1,v2) # let v1 be the smaller number
    while root != None:
        if root.info == v1 or root.info == v2:
            return root
        elif v1 < root.info and root.info < v2:
            return root
        else:
            if v1 > root.info:
                return lca(root.right, v1, v2)
            else:
                return lca(root.left, v1, v2)
    return None
