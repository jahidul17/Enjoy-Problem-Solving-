import math
a,b,c=list(map(float,input().split()))

d=b**2-4*a*c

if a==0 or d<0:
    print("Impossivel calcular")
    
else:
    x1=(-b + math.sqrt(d))/(2*a)
    x2=(-b - math.sqrt(d))/(2*a)
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")
