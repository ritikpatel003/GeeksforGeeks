class Solution:
    def isAmicable(self, A , B):
        # code here 
        import math
        d1=1
        d2=1
        if A<=2 and B<=2:
            return 0
        for i in range(2,int(math.sqrt(A))+1):
            if A%i==0:
            	d1+=(A//i+i)
        for i in range(2,int(math.sqrt(B))+1):
            if B%i==0:
            	d2+=(B//i+i)
        if d1==B and d2==A:
        	return 1
        else:
        	return 0