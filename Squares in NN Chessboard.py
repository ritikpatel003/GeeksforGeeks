class Solution:
    def squaresInChessBoard(self, N):
        # code here
        res=0
        while(N>0):
            res+=N**2
            N-=1
        return res