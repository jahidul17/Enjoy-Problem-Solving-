n=int(input())
for i in range(1,n+1):
    x=int(input())
    if (not x):
      print("0 ") # handling the case when x is 0
    else:
        while x>0:
            r=x%10
            print(r,end=" ")
            x=x//10

        print()
    

