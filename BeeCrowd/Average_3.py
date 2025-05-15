n1,n2,n3,n4=list(map(float,input().split()))
# print(n1,n2,n3,n4)
avg=(n1*2+n2*3+n3*4+n4*1)/(1+2+3+4)

print(f"Media: {avg:.1f}")

if avg>=7:
    print("Aluno aprovado.")
elif avg<5:
    print("Aluno aprovado.")
elif avg>=5 and avg<=6.9:
    print("Aluno em exame.")   
    n5=float(input())
    print(f"Nota do exame: {n5:.1f}")
    avg2=(n5+avg)/2


