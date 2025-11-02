n=int(input())
primary=[]
for i in range(n):
    for j in range(n):
        lis=list(map(int, input().split()))
        # print(lis)
        if(i==j):
            primary.append(i)
            
for v in primary:
    print(v)


