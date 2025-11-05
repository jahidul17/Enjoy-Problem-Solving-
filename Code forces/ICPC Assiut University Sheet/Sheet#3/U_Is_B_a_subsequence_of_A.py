n,m=map(int, input().split())

a=list(map(int, input().split()))
b=list(map(int, input().split()))

# print(a)
# print(b)

i=0
j=0
while i<n and j<m:
    if a[i]==b[j]:
        j=j+1
    i=i+1


if j == m:
    print("YES")
else:
    print("NO")
    
 
 
 