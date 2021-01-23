N=324
x=[]
n=len(str(N))+1
for i in range(1,n):
	for j in range(1,n):
		x.append(N%10**j)
	n-=1
	N=N//10
flag=1
s={}
for i in x:
	p=1
	while(i>1):
		p*=i%10
		i//=10
	if p not in s:
		s[p]=1
	else:
		flag=0
print(flag)
