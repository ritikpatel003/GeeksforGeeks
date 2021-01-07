'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
res=[0]
def sol(x,i):
    if x==None:
        if res[0]<i:
            res[0]=i
        return i
    sol(x.left,i+1)
    sol(x.right,i+1)
    return res[0]
print(sol(root,0))