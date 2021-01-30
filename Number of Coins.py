class Solution:
	def minCoins(self, coins, M, V):
		# code here
        w=V
        n=M
        dp=[[0 for i in range(w+1)] for j in range(n+1)]
        for i in range(w+1):
        	if i%coins[0]==0:
        		dp[1][i]=i//coins[0]
        	else:	
        		dp[1][i]=2**32-1
        for i in range(2,n+1):
        	for j in range(1,w+1):
        		if j>=coins[i-1]:
        			dp[i][j]=min(1+dp[i][j-coins[i-1]],dp[i-1][j])
        		else:
        			dp[i][j]=dp[i-1][j]
        if dp[n][w]>2**30:
            return -1
        return(dp[n][w])