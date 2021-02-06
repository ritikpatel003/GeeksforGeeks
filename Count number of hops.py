def countWays(n):
    '''
    :param n: given value of n
    :return: Integer , ways to write n as sum of positive integers
    '''
    # code here
    dp=[1,1,2]
    if n>=3:
    	for i in range(3,n+1):
    		dp.append((dp[i-1]+dp[i-2]+dp[i-3])%1000000007)
    return dp[n]