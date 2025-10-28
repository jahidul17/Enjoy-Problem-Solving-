
test=int(input())
for i in range(test):
    n=int(input())
    s,t=map(str,input().split())
    
    if sorted(s)==sorted(t):
        print("YES")
    else:
        print("NO")
        


