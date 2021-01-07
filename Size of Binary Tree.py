def getSize(node):
    # code here
    res=[0]
    def sol(x):
        if x==None:
            return 0
        res[0]+=1
        sol(x.left)
        sol(x.right)
        return res[0]
    return sol(node)