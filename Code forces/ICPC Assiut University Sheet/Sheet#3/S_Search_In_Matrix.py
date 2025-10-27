n,m=map(int,input().split())


matrix = []
for i in range(1,n+1):
    row=list(map(int, input().split()))
    matrix.append(row)
#or
# A = [list(map(int, input().split())) for _ in range(N)]

x=int(input())

flag=False

for row in matrix:
    if x in row:
        flag=True
        break
    else:
        continue
    
if flag:
    print("will not take number")
else:
    print("will take number")
