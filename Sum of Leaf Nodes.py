'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def sumLeaf(root):
    '''
    :param root: root of given tree.
    :return: sum of leaf nodes
    '''
    # code here
    res=[0]
    def sol(x):
        if x!=None:
            if x.right==None and x.left==None:
                res[0]+=x.data
                return 0
            sol(x.left)
            sol(x.right)
        return res[0]
    return sol(root)