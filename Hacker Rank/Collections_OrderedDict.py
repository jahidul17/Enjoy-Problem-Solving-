from collections import OrderedDict

a = OrderedDict()
input_ = int(input())
for _ in range(input_):
    item, space, price = input().rpartition(' ')
    #the str.rpartition(sep) method splits a string into three parts
    a[item] = a.get(item, 0) + int(price)

for item, price in a.items():
    print(item, price)

