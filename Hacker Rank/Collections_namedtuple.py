from collections import namedtuple

n=int(input())

fields=input().split()
total_marks=0
for i in range(n):
    # students=namedtuple('my_student','')
    students = namedtuple('my_student', fields)
    MARKS, CLASS, NAME, ID = input().split()
    my_student = students(MARKS, CLASS, NAME, ID)
    total_marks += int(my_student.MARKS)
print((total_marks / n))
    

