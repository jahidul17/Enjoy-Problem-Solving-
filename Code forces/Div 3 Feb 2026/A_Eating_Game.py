t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    maximum=max(arr)
    count=arr.count(maximum)
    print(count)

