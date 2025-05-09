a=input().split(' ')[1:]
b=input().split(' ')[1:]
total=int(a[0])*float(a[1])+int(b[0])*float(b[1])

# a=[float(a) if '.' in a else int(a) for a in input().split(' ')[1:]]
# b=[float(a) if '.' in a else int(a) for a in input().split(' ')[1:]]


# a=[int(a) if a.isdigit() else float(a) for a in input().split(' ')[1:]]#int mean true and float means false
# b=[int(a) if a.isdigit() else float(a) for a in input().split(' ')[1:]]

# total=a[0]*a[1] + b[0]*b[1]

print(f"VALOR A PAGAR: R$ {total:.2f}")


