'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''
def maxLevelSum(root):
    # Code here
    res=[0]
    def sol(x,k):
        if x!=None:
            if x.left==None and x.right==None:
                if k>res[0]:
                    res[0]=k
            sol(x.left,k+1)
            sol(x.right,k+1)
        return res[0]
    res=[0]*(sol(root,0)+1)
    def sol(x,k):
        if x!=None:
            res[k]+=x.data
            sol(x.left,k+1)
            sol(x.right,k+1)
        return res
    return max(sol(root,0))