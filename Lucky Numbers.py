def isLucky(n):
    #RETURN 1 OR 0
    flag=[0]
    if n==1:
        return 1
    def sol(n,x):
    	if n%x==0:
    		return
    	if n-n//x<=x:
    		if n-n//x==x:
    			flag[0]=1
    		return
    	sol(n-n//x,x+1)
    	return 0
    sol(n,2)
    return(flag[0])