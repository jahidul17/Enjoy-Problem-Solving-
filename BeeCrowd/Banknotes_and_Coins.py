n=float(input())

print("NOTAS:")
for i in [100,50,20,10,5,2]:
    print(f"{int(n/i)} nota(s) de R$ {i}.00")
    n=float(f"{n%i:.2f}")
    
print("MOEDAS:")

for i in [1.00,0.50,0.25,0.10,0.05,0.01]:
    print(f"{int(n/i)} moeda(s) de R$ {i:.2f}")
    n=float(f"{n%i:.2f}")

