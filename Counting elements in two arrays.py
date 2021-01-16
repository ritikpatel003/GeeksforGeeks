m=6
n=6
arr1=[1,2,3,4,7,9]
arr2=[0,1,2,1,1,4]
a=arr1
b=sorted(arr2)
res=[]
for i in a:
	l=0
	r=n-1
	while(r>=l):
		m=(l+r)//2
		if b[m]<=i:
			l=m+1
		else:
			r=m-1
	res.append(r+1)
print(res)    