t=int(input())

for _ in range(t):
    x=list(map(int,input().split()))
    res=sum(x)
    print(2*max(x)-res)


