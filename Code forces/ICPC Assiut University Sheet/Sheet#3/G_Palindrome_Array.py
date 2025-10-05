
n=int(input())
m=list(map(int, input().split()))

o=m[::-1]

if(o==m):
    print("YES")
else:
    print("NO")
