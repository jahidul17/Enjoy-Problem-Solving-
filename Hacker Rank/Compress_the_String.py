from itertools import groupby
# from itertools import *
# * means all function
n=input()

for i, j in groupby(n):
    # print(list(j),int(i))
    print(tuple([len(list(j)),int(i)]),end=" ")
