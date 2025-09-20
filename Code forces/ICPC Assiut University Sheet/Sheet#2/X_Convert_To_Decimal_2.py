# m = int(input())  # decimal number

# for i in range(1,m+1):
#     n=int(input())
#     res = ''  # binary result

#     while n > 0:
#         temp = str(n % 2)
#         res=temp+res
#         # print(res)
#         n //= 2
#     # print(res)

#     bin=''
#     ch=list(res)
#     # print(ch)
#     for i in ch:
#         if(i=='1'):
#             bin=i+bin
#             # print(i)
#     print(int(bin, 2))



# Using built in function Binary to Decimal 

# for b in ['100', '101']:
#     print(int(b, 2))


# anothor way

m = int(input()) 

for i in range(1,m+1):
    n=int(input())
    res = ''

    while n > 0:
        temp = str(n % 2)
        if(temp=='1'):
            res=temp+res
        n //= 2
    print(int(res, 2))


