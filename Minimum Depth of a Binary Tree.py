'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

def minDepth(root):
    res=[2**32-1]
    def sol(x,k):
        if x!=None:
            if x.left==None and x.right==None:
                if k<res[0]:
                    res[0]=k
                return 0
            sol(x.left,k+1)
            sol(x.right,k+1)
        return res[0]
    return sol(root,1)