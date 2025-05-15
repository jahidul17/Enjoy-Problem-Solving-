x,y=list(map(int,input().split()))

price=[4.00,4.50,5.00,2.00,1.50]
# price=[0,4.00,4.50,5.00,2.00,1.50] #another way need not use x-1

pay=price[x-1]*y
print(f"Total: R$ {pay:.2f}")

# if 5.00 in price:
#     print(price.index(5.00))



