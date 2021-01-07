##Structure of the node
'''
class Node:
    data=0
    left=None
    right=None

'''

def minValue(root):
    ##Your code here
    res=[0]
    def sol(x):
        if x.left==None:
            res[0]=x.data
            return x.data
        sol(x.left)
        return res[0]
    return sol(root)