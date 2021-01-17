class Solution:
	def findPeakElement(self, a):
		# Code here
		if a[0]>a[1]:
		    return a[0]
		if a[len(a)-1]>a[len(a)-2]:
		    return a[len(a)-1]
        l=1
        r=len(a)-2
        while(r>=l):
            m=(l+r)//2
            if a[m]>a[m-1] and a[m]>a[m+1]:
                break
            elif a[m]>a[m-1]:
                l=m+1
            else:
                r=m-1
        return(a[m])