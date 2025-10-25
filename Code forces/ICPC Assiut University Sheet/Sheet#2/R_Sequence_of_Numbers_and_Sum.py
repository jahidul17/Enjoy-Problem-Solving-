
while(True):
    m,n=map(int, input().split())
    if(m<=0 or n<=0):
        break

    if m>n:
        sum=0
        for i in range(n,m+1):
            sum+=i
            print(i,end= " ")
        print(f"sum ={sum}")
    else:
        sum=0
        for i in range(m,n+1):
            sum+=i
            print(i,end=" ")
        print(f"sum ={sum}")
    
    


    