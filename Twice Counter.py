class Solution:
    def countWords(self,List, n):
        #code here
        d={}
        for i in List:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        res=0
        for i in list(d.keys()):
            if d[i]==2:
                res+=1
        return res