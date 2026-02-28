n=int(input())

for _ in range(n):
    s,t=input().split()

    
    minimum=min(len(s),len(t))
    
    result=""
    for i in range(minimum):
        result+=s[i]+t[i]

    if len(s)>len(t):
        result+=s[minimum:]
    else:
        result+=t[minimum:]
        
    print(result)


