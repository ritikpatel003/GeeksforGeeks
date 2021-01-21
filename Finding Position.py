#code
for t in range(int(input())):
    n=int(input())
    a=[]
    for i in range(n+1):
        a.append(i+1)
    def sol(a):
        if len(a)==1:
            print(a[0])
            return
        b=[]
        for i in range(1,len(a),2):
            b.append(a[i])
        sol(b)
        return 
    sol(a)