n=int(input())
m=list(map(int,input().split()))


small=min(m)
index=m.index(small)+1
print(f"{small} {index}")



#Another way
#Manula method.

# small=m[0]
# # index=1
# # print(m)
# for i in range(1,n):
#     if(small<m[i]):
#         continue
#     else:
#         small=m[i]
#         # index=i+1
    
# print(small,end=' ')
# print(m.index(small)+1)

