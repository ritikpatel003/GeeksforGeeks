'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# Return a list containing the inorder traversal of the given tree
def InOrder(root):
    # code here
    res=[]
    def sol(x):
        if x!=None:
            sol(x.left)
            res.append(x.data)
            sol(x.right)
        return res
    return sol(root)