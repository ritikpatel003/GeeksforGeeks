#code
for t in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    count=0
    for i in range(1,n+1):
        flag=0
        for j in a:
            if i%j==0:
                flag=1
                break
        if flag==0:
            count+=1
    print(count