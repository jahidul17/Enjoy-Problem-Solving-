# from collections import namedtuple

# n=int(input())

# fields=input().split()
# total_marks=0
# for i in range(n):
#     # students=namedtuple('my_student','')
#     students = namedtuple('my_student', fields)
#     MARKS, CLASS, NAME, ID = input().split()
#     my_student = students(MARKS, CLASS, NAME, ID)
#     total_marks += int(my_student.MARKS)
# print((f'{total_marks / n:.2f}'))

from collections import namedtuple

n = int(input())
fields = input().split()

Student = namedtuple('Student', fields)  # Define namedtuple once

total_marks = 0
for _ in range(n):
    data = input().split()
    student = Student(*data)
    total_marks += int(student.MARKS)

print(f'{total_marks / n:.2f}')


