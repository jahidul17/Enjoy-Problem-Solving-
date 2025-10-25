n=int(input())
num=list(map(int,input().split()))
target=int(input())
flag=0
for i in num:
    if(i==target):
        print(num.index(i))
        flag=1
        break

if (flag==False):
    print("-1")
