'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return true/false or 1/0

def isIdentical(root1, root2):
    # Code here
    flag=[0]
    def sol(x,y):
        if x!=None and y!=None:
            if x.data!=y.data:
                flag[0]=1
                return 0
            sol(x.left,y.left)
            sol(x.right,y.right)
        elif x!=None or y!=None:
            flag[0]=1
            return
        return
    sol(root1,root2)
    if flag[0]==1:
        return False
    else:
        return True