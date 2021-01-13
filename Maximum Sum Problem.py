n=24
a=[0,1,2,3]
for i in range(4,n+1):
	a.append(max(a[i//2]+a[i//3]+a[i//4],i))
print(a[n])