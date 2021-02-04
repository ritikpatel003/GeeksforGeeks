class Solution:
    def merge(self, arr1, arr2, n, m): 
        # code here
        A=arr1
        B=arr2
        a=[]
        i=j=0
        while(i<len(A) or j<len(B)):
            if A[i]<B[j]:
                a.append(A[i])
                i+=1
            else:
                a.append(B[j])
                j+=1
            if j==len(B):
                a+=A[i::]
                break
            elif i==len(A):
                a+=B[j::]
                break
        for i in range(len(arr1)):
            arr1.pop(-1)
        for i in range(len(arr2)):
            arr2.pop(-1)
        arr1.append(a[0])
        for i in a[1::]:
            arr2.append(i)