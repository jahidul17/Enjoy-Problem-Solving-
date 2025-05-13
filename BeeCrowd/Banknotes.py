n=int(input())
print(n)
for i in [100,50,20,10,5,2,1]:
    print(f"{n//i} nota(s) de R$ {i},00")
    n=n%i

