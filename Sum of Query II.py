#code
from math import *
for t in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    q=int(input())
    w=list(map(int, input().split()))
    res=[]
    for i in range(0,2*q,2):
        l=w[i]
        r=w[i+1]
        res.append(sum(a[l-1:r]))
    print(*res)