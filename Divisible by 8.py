#code
for t in range(int(input())):
    x=int(input())
    x=str(x)
    n=list(x)
    d={}
    flag=0
    if len(x)==1:
        if int(n)%8==0:
            print("Yes")
        else:
            print("No")
    if len(x)==2:
        if int(x)%8==0 or int(str(x[-1])+str(x[0]))%8==0:
            print("Yes")
        else:
            print("No")
    else:    
        for i in n:
        	if int(i) not in d:
        		d[int(i)]=1
        	else:
        		d[int(i)]+=1
        for i in range(104,1000,8):
        	e={}
        	for j in str(i):
        		if int(j) not in e:
        			e[int(j)]=1
        		else:
        			e[int(j)]+=1
        	count=0
        	for k in list(e.keys()):
        		if k in d:
        			count+=min(e[k],d[k])
        	if count==3:
        		flag=1
        		print("Yes")
        		break
        if flag==0:
        	print("No")


