n=int(input())
s=input()

count=1

for x in range(1,n):
    if s[x]!=s[x-1]:
        count+=1
        
print(count)
