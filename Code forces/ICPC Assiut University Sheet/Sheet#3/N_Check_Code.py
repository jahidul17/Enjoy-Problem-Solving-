a,b=map(int,input().split())

s=input()

if len(s)!=a+b+1:
    print("No")
else:
    if s[a]!='-':
        print("No")
    else:
        part1=s[:a]
        part2=s[a+1:]
        if part1.isdigit() and part2.isdigit():
            print("Yes")
        else:
            print("No")

