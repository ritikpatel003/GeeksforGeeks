def sumBT(root):
    #code
    res=[0]
    def sol(x):
        if x==None:
            return 0
        res[0]+=x.data
        sol(x.left)
        sol(x.right)
        return res[0]
    return sol(root)