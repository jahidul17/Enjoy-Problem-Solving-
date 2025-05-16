
a,b,c=sorted(list(map(float,input().split())),reverse=True)

# sort() in Python function is very similar to sorted() but unlike sorted it returns nothing and makes changes to the original sequence. 

if a>=(b+c):print("NAO FORMA TRIANGULO")
elif a**2==(b**2) + (c**2):print("TRIANGULO RETANGULO")
elif a**2>(b**2) + (c**2):print("TRIANGULO OBTUSANGULO")
elif a**2<(b**2) + (c**2):print("TRIANGULO ACUTANGULO")
if a==b==c:print("TRIANGULO EQUILATERO")
elif a==b or b==c:print("TRIANGULO ISOSCELES")
