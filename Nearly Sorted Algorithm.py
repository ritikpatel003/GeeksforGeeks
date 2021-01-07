import heapq
from math import *
for t in range(int(input())):
    n,k=map(int, input().split())
    a=list(map(int, input().split()))
    heapq.heapify(a)
    res=[]
    while(a!=[]):
        res.append(a[0])
        heapq.heappop(a)
    print(*res)