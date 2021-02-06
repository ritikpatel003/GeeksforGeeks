a=3
b=4
dp=[[1 for i in range(a)] for j in range(b)]
for j in range(b-2,-1,-1):
	for i in range(a-2,-1,-1):
		dp[j][i]=dp[j+1][i]+dp[j][i+1]
print(dp[0][0])