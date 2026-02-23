n,q=map(int,input().split())

arr=set(map(int,input().split()))

for _ in range(q):
    x=int(input())
    if x in arr:
        print('found')
    else:
        print('not found')



