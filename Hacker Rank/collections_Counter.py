
n=int(input())

stock=list(map(int,input().split()))

# print(stock)

from collections import Counter

# Returns an iterator over elements repeating as per their counts.
dict=Counter(stock)

# print(dict)
# print(dict[5])

x=int(input())

p=0
for i in range(x):
    size,price=map(int,input().split())
    # print(size,price)
    if dict[size]:
        # print(dict[size])
        dict[size]=dict[size]-1        
        p=p+price
        
print(p)


