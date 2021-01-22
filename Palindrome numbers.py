class Solution:
    def isPallindrome(self, N):
        # code here
        s=""
        while(N>0):
            s+=str(N%2)
            N//=2
        if s==s[::-1]:
            return 1
        else:
            return 0