from collections import defaultdict

n,m= map(int,input().split())

d= defaultdict(list)

for i in range(n):
    ans1=input()
    d[ans1].append(i+1)
    
for j in range(m):
    ans2=input()
    if ans2 in d:
        print(*d[ans2]) #*d[ans2]: unpacks the iterable (like a list or tuple) into separate arguments.
        # print(d[ans2])
    else:
        print(-1)