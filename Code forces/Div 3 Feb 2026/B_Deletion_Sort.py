t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    flag=False
    if(len(arr)>1):
        for i in range(len(arr)-1):
            if(arr[i]>arr[i+1]):
                flag=True
                break
        # print(arr[i])
    
    if (flag==True):
        print(1)
    else:
        print(len(arr))        
    
    



