n = 9
arr = [1,15,25,45,42,21,17,12,11]
l=0
r=n-1
while(l<=r):
	m=(l+r)//2
	if m==0 and arr[m]>arr[m+1]:
		print(arr[m])
		break
	elif m==n-1 and arr[m]>arr[m-1]:
		print(arr[m])
		break
	elif arr[m]>arr[m-1] and arr[m]>arr[m+1]:
		print(arr[m])
		break
	else:
		if m==0:
			l=m+1
		elif m==n-1:
			r=m-1
		else:
			if arr[m+1]>arr[m-1]:
				l=m+1
			else:
				r=m-1
