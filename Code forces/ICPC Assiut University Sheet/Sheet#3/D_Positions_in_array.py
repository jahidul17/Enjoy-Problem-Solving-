
n=int(input())

num=list(map(int,input().split()))


for i, X in enumerate(num):
    if X <= 10:
        print(f"A[{i}] = {X}")
        

# Duplicate value issue.
"""Correctness: The list.index() method returns the index of the first occurrence of a value. If your list has duplicate numbers less than or equal to 10, your code will fail to print the correct index for duplicates after the first one. For example, in the list [1, 5, 20, 5], num.index(5) will always return 1, even for the second 5. enumerate, however, correctly handles this by providing a unique index for each element as it iterates."""
# for i in num:
#     if(i<11):
#         print(f"A[{num.index(i)}] = {i}")
    



