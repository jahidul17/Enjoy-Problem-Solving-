#Haven't Solved

t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    
    arr.sort()
    # print(arr)
    
    result=10**18
    # ans = float('inf')
    # print(result)
    
    for i in range(n-1):
        result=min(result,arr[i+1]-arr[i])
    print(result)
