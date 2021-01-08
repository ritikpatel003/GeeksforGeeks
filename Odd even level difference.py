'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
def getLevelDiff(root):
    # Code here
    a=[0,0]
    def sol(x,k):
        if x!=None:
            if k%2==0:
                a[0]+=x.data
            else:
                a[1]+=x.data
            sol(x.left,k+1)
            sol(x.right,k+1)
        return a[0]-a[1]
    return sol(root,0)