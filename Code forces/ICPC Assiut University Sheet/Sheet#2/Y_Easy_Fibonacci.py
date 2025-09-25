n=int(input())

f1=0
f2=1

for i in range(1,n+1):
    if(n==1):
        print(0)
    elif(n==2):
        print(f"0 1 ")
        break
    else:
        if(i==1):
            print(f"0 1 ",end="")
        fibo=f1+f2
        print(fibo,end=" ")
        f1=f2
        f2=fibo
        if(n-2==i):
            break

print()
