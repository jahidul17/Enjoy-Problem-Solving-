
row,col=map(int,input().split(' '))

for i in range(1,row,2):
    print((".|."*i).center(col,'-'))

print("WELCOME".center(col,'-'))

for i in range(row-2,-1,-2):
    print((".|."*i).center(col,'-'))