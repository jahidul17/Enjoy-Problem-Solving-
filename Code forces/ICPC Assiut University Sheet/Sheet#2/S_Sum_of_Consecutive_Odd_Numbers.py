n=int(input())
while(n>0):
    x,y=map(int,input().split())
    if(x>y):
        sum=0
        for i in range(y+1,x):
            if(i%2 != 0):
                sum+=i
        print(sum)
    else:
        sum=0
        for i in range(x+1,y):
            if(i%2 != 0):
                sum+=i
        print(sum)
    n=n-1
    