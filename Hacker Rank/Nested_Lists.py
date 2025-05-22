students=[]

for _ in range(int(input())):
    name=input()
    score=float(input())
    
    students.append([name,score])
    

second_highest=set([score for name,score in students])
second_highest=sorted(second_highest)[1]

# second_highest = sorted(set([score for name, score in students]))[1]

# print('\n'.join(sorted([name for name, score in students if score == second_highest])))

name_app=[]

for name, score in students:
    if score == second_highest:
        name_app.append(name)
        
# print(.join(sorted(name_app))) #error
# print(''.join(sorted(name_app)))
print('\n'.join(sorted(name_app)))



