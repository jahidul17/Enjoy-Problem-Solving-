nowsal=float(input())

if nowsal<=400:
    percentage=15

elif nowsal<=800:
    percentage=12
elif nowsal<=1200:
    percentage=10
elif nowsal<=2000:
    percentage=7
else:
    percentage=4

earn=nowsal*percentage/100
newsal=nowsal+earn

print(f"Novo salario: {newsal:.2f}\nReajuste ganho: {earn:.2f}\nEm percentual: {percentage} %")

