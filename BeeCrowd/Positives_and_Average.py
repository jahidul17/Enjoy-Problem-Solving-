# count=0
# sum=0

# for i in range(6):
#     m=float(input())
#     if m>0:
#         count+=1
#         sum=sum+m
        
# print(f"{count} valores positivos")
# print(sum/count)

# 2nd way 


count=[]

for i in range(6):
    m=float(input())
    if m>0:
        count.append(m)

print(f'{len(count)} valores positivos')
print(f"{sum(count)/len(count):.1f}")




