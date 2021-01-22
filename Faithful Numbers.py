class Solution:
    def nthFaithfulNum(self, N):
        # code here 
        s=""
        while(N>0):
            s+=str(N%2)
            N//=2
        res=0
        c=0
        for i in s:
            if i=="1":
                res+=7**c
            c+=1
        return res