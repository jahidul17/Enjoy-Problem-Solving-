
n=int(input())
num=list(map(int,input().split()))

store=[]

for i in num:
    if(i==0):
        store.append(0)
    elif(i<0):
        store.append(2)
    elif(i>0):
        store.append(1)
        
# Print without using any separators between elements
print(*store)

# Print using separator (,)
# print(*a, sep =', ')
