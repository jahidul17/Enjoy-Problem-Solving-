a, b = map(int, input().split())

unlcky=False
for i in range(a,b+1):
    count=i
    lucky=False
    
    while count:
        if count%10 !=7 and count%10 !=4:
            lucky=True
        count//=10
    
    if lucky==False:
        print(i,end=" ")
        unlcky=True
        
if unlcky==False:
    print(-1)



# --------------------------


# a, b = map(int, input().split())

# unlucky = 0

# for i in range(a, b + 1):
#     count = i
#     lucky = 0

#     while count:
#         if count % 10 != 7 and count % 10 != 4:
#             lucky += 1
#         count //= 10


#     if lucky == 0:
#         print(i, end=' ')
#         unlucky += 1

# if unlucky == 0:
#     print("-1")

