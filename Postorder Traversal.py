'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def postOrder(root):
    '''
    :param root: root of the given tree.
    :return the list containing post order traversal of the given binary tree.
    '''
    # code here
    res=[]
    def sol(x):
        if x!=None:
            sol(x.left)
            sol(x.right)
            res.append(x.data)
        return res
    return sol(root)