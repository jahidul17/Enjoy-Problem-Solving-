# Program is run but TLE issue that's way not accepet and It's use recurson
# def fibo(n):
#     if(n==1):
#         return 0
#     elif(n==2):
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)

# n=int(input())

# print(fibo(n))

# ------------------------------


# Optimize way O(n) time complexity

n=int(input())

f1=0
f2=1

arr=[]

for i in range(1,n+1):
    if(n==1):
        # print(0)
        arr.append(0)
    elif(n==2):
        # print(f"0 1 ")
        arr.extend([0,1])
        break
    else:
        if(i==1):
            # print(f"0 1 ",end="")
            arr.extend([0,1])
        fibo=f1+f2
        # print(fibo,end=" ")
        arr.append(fibo)
        f1=f2
        f2=fibo
        if(n-2==i):
            break

# print(arr)
print(arr[n-1])

# ----------------------------------

# Optional (Efficient Version)


# N = int(input())
# a, b = 0, 1
# for _ in range(2, N):
#     a, b = b, a + b
# print(a if N == 1 else b)

