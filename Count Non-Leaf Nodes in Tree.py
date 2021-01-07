# function should return the count of total number of non leaf nodes in the tree
def countNonLeafNodes(root):
    
    # add code here
    res=[0]
    def sol(x):
        if x==None:
            return 0
        if x.left!=None or x.right!=None:
            res[0]+=1
        sol(x.left)
        sol(x.right)
        return res[0]
    return sol(root)