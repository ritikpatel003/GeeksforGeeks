#code
for t in range(int(input())):
    n=int(input())
    n=[n]
    res=[0]
    def sol(i,c):
        pd=1
        for x in range(c):
            i+=1
            pd*=i
        res[0]+=pd
        if c==n[0]:
            print(res[0])
            return
        sol(i,c+1)
    sol(0,1)