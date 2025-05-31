
from itertools import product

a=list(map(int,input().split()))
b=list(map(int,input().split()))

# axb=product(a,b)

# for i in axb:
#     print(i, end=" ")


# or 

pack=list(product(a,b))
# print(pack)

# The asterisk * is the unpacking operator.
#unpack
print(*pack)



