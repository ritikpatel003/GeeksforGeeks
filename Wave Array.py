class Solution:
    #Complete this function
    def convertToWave(self,A,N):
        #Your code here
        for i in range(0,N-1,2): 
            A[i], A[i+1] = A[i+1], A[i]