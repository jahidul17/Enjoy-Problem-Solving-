n=int(input())
num=list(map(int,input().split()))

max_digit=num[0]

for i in num:
    if i>max_digit:
        max_digit=i

print(max_digit)

# another way
# print(max(num))
