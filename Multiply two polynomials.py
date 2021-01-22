class Solution:
	def polyMultiply(self, Arr1, Arr2, M, N):
		# code here
        res=[0]*(M+N-1)
        for i in range(M):
            for j in range(N):
                res[i+j]+=Arr1[i]*Arr2[j]
        return res