def productExceptSelf(arr, n):
    #code here
    p=1
    for i in arr:
        p*=i
    res=[]
    for i in range(n):
        if arr[i]==0:
            pr=1
            for x in range(i):
                pr*=arr[x]
            for x in range(n-1,i,-1):
                pr*=arr[x]
            res.append(pr)
        else:
            res.append(p//arr[i])
    return res