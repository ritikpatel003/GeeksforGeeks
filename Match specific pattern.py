Dict = ["abb","abc","xyz","xyy"]
pattern  = "foo"

def sol(s):
	d={}
	for i in s:
		if i in d:
			d[i]+=1
		else:
			d[i]=1
	return list(d.values())

x=sol(pattern)
res=[]

for i in Dict:
	y=sol(i)
	if x==y:
		res.append(i)
print(res)

