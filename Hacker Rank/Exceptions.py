
n=int(input())

for i in range(n):
    try:
        a,b=list(map(int,input().split()))
        print(int(a//b))
    except Exception as e:
        print("Error Code:",e)

