'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def rightView(root):
    '''
    :param root: root of given tree.
    :return: the right view of tree,
    '''
    # code here
    res={}
    def sol(x,k):
        if x!=None:
            res[k]=x.data
            sol(x.left,k+1)
            sol(x.right,k+1)
        return res
    sol(root,0)
    return list(res.values())