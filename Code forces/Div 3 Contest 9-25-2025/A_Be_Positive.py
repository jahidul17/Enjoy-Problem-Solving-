#Solved

t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    
    totalNeg=arr.count(-1)
    totalZero=arr.count(0)
    
    if(totalNeg%2==0):
        result=totalZero
    else:
        result=totalZero+2
        
    print(result)


