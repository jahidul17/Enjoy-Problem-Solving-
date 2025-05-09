
a,b,c=list(map(float,input().split()))

triangle=.5*a*c
circle=3.14159*c*c
trapizium=.5*(a+b)*c
square=b*b
rectangle=a*b

print(f"""TRIANGULO: {triangle:.3f}
CIRCULO: {circle:.3f}
TRAPEZIO: {trapizium:.3f}
QUADRADO: {square:.3f}
RETANGULO: {rectangle:.3f}""")

