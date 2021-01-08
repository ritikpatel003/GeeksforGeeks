'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def preorder(root):
    '''
    :param root: root of the given tree.
    :return: a list containing pre order Traversal of the given tree.
    {
        class Node:
        def _init_(self,val):
            self.data = val
            self.left = None
            self.right = None
    }
    '''
    # code here
    res=[]
    def sol(x):
        res.append(x.data)
        if x.left==None and x.right==None:
            return res
        if x.left!=None:
            sol(x.left)    
        if x.right!=None:
            sol(x.right)
        return res
    return sol(root)