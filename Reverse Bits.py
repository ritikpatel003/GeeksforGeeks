class Solution:
    def reversedBits(self, X):
        # code here 
        s=""
        while(X>0):
            s+=str(X%2)
            X//=2
        res=0
        c=31
        for i in s:
            if i=="1":
                res+=2**c
            c-=1
        return res