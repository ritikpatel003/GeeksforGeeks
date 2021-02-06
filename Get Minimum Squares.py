class Solution:
	def MinSquares(self, n):
		# Code here
        dp=[n for i in range(n+1)]
        dp[0]=0
        for i in range(1,n+1):
        	for j in range(1,int(i**(1/2)+1)):
        		ms=1+dp[i-j**2]
        		dp[i]=min(ms,dp[i])
        return dp[-1]