t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))

    answer=float('inf')
    
    for i in range(n):
        for j in range(i+1,n):
            value=arr[i]+arr[j]+(j-i)
            answer=min(answer,value)
            
    print(answer)


        





