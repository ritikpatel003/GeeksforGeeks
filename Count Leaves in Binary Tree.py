'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
def countLeaves(root):
    # Code here
    res=[0]
    def sol(x):
        if x.right==None and x.left==None:
            res[0]+=1
            return 0
        if x.left!=None:
            sol(x.left)
        if x.right!=None:
            sol(x.right)
        return res[0]
    return sol(root)