class Solution:
    def quickExponents(self, N):
    	#code here 
    	res=0
    	while(N>=5):
    	    res+=N//5
    	    N//=5
    	return res