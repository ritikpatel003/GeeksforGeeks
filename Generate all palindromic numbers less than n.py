class Solution:
    def palindromicNumbers(self, N):
    	#code here 
    	count=0
        for i in range(1,N):
            if str(i)==str(i)[::-1]:
                count+=1

        return count