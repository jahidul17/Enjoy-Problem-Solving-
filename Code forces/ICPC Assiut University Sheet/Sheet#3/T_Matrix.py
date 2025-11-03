
rows = int(input())

matrix = []

for i in range(rows):
    element = list(map(int,input().split()))
    matrix.append(element)

primary_add=0
for i in range(len(matrix)):
    # print(matrix[i][i])
    primary_add=primary_add+matrix[i][i]
    
secondary_add=0
for i in range(len(matrix)):
    # print(matrix[i][len(matrix)-1-i])
    secondary_add=secondary_add+matrix[i][len(matrix)-1-i]
    
result=int(abs(primary_add-secondary_add))
print(result)
