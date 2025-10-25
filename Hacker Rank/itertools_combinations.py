from itertools import combinations

s,n=input().split()

for i in range(1,int(n)+1):
    for j in list(combinations(sorted(s),int(i))):
        print("".join(j))
