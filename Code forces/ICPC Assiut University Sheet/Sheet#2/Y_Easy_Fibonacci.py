n=int(input())

f1=0
f2=1
print(f"{f1} {f2}",end=" ")

for i in range(1,n-1):
    fibo=f1+f2
    print(fibo,end=" ")
    f1=f2
    f2=fibo


