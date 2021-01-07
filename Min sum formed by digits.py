import heapq
for t in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    heapq.heapify(a)
    x=""
    y=""
    while(a!=[]):
        x+=str(a[0])
        heapq.heappop(a)
        if a==[]:
            break
        y+=str(a[0])
        heapq.heappop(a)
    print(int(x)+int(y))