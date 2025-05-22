
# 1st way 
# n=1
# while n<=100:
#     if n%2==0:
#         print(n)
#     n=n+1

# 2nd way 

# for i in range(2,101,2):
#     print(i)


# 3rd way 
# [print(i) for i in range(1,101) if i%2==0]

# 4th way 

def even(n):
    if n%2==0 and n!=100:
        print(n)
    if n==100:
        return print(n)
    return even(n+1)

even(1)
