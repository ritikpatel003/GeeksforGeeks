'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
def mirror(root):
    # Code here
    res=[]
    def sol(x):
        if x!=None:
            temp=x.left
            x.left=x.right
            x.right=temp
            sol(x.left)
            sol(x.right)
        return res
    sol(root)
    return