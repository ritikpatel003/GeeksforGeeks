n = 6
arr = [0,0,0,0,0,0]
l=0
r=n-1
res=0
if arr[0]==0 and arr[-1]==0:
	print(n)
elif arr[0]==1 and arr[-1]==1:
	print(0)
elif arr[0]==1:
	while(l<=r):
		m=(l+r)//2
		if arr[m]==1 and arr[m+1]==0:
			res=m
			break
		if arr[m]==1:
			l=m+1
		else:
			r=m-1
	print(n-res-1)
elif arr[0]==0:
	while(l<=r):
		m=(l+r)//2
		if arr[m]==0 and arr[m+1]==1:
			res=m
			break
		if arr[m]==0:
			l=m+1
		else:
			r=m-1
	print(res+1)