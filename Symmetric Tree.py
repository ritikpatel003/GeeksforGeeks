def isSymmetric(root):
    # Your Code Here
    res1=[]
    res2=[]
    def sol1(x):
        if x!=None:
            res1.append(x.data)
            sol1(x.left)
            sol1(x.right)
    def sol2(x):
        if x!=None:
            res2.append(x.data)
            sol2(x.right)
            sol2(x.left)
    flag=0
    try:
        sol1(root.left)
    except:
        flag+=1
    try:
        sol2(root.right)
    except: 
        flag+=1
    if flag==1:
        return False
    return res1==res2