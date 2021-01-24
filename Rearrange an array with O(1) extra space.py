def arrange(arr, n): 
    #Your code here
    res=[]
    for i in arr:
        res.append(arr[i])
    for i in res:
        arr.pop(0)
        arr.append(i)
    return