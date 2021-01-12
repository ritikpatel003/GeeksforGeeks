a=3
b=2
dp=[]
for i in range(b+1):
	dp.append((a+1)*[0])
for i in range(a+1):
	dp[0][i]=1
for i in range(b+1):
	dp[i][0]=1
for i in range(1,b+1):
	for j in range(1,a+1):
		dp[i][j]=dp[i-1][j]+dp[i][j-1]
print(dp[b][a])
