'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#Complete the function below
def verticalSum(root):
    #:param root: root of the given tree.
    
    #code here
    d={}
    def sol(x,k):
        if x!=None:
            if k in d:
                d[k]+=x.data
            else:
                d[k]=x.data
            sol(x.left,k-1)
            sol(x.right,k+1)
        return k
    sol(root,0)
    res=[]
    for i in sorted(d) :
        res.append(d[i])
    return res