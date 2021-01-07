import heapq
n = 5
a= [4, 2, 7, 6, 9]
heapq.heapify(a)
res=0
while(a!=[]):
    x=0
    res+=a[0]
    x+=a[0]
    heapq.heappop(a)
    if a==[]:
        break
    res+=a[0]
    x+=a[0]
    heapq.heappop(a)
    heapq.heappush(a,x)
print(res-x)