'''
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def KDistance(root,k):
    '''
    :param root: root of given tree.
    :param k: distance k from root
    :return: Print all nodes that are at distance k from root, no need to print next line.
    '''
    # code here
    res=[]
    K=[k]
    def sol(x,a):
        if x!=None:
            if a==K[0]:
                res.append(x.data)
            sol(x.left,a+1)
            sol(x.right,a+1)
        return res
    return sol(root,0)