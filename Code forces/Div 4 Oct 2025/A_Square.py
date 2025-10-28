n=int(input())

for i in range(n):
    lis=list(map(int,input().split()))
    if len(set(lis))==True:
        print("YES")
    else:
        print("NO")


