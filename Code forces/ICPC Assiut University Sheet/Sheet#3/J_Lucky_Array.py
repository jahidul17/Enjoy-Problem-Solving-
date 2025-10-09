n=int(input())

num=list(map(int, input().split()))

min=min(num)
count=num.count(min)

if(count%2==0):
    # print(count)
    print("Unlucky")
elif(count%2!=0):
    # print(count)
    print("Lucky")

