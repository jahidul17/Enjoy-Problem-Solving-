if __name__ == '__main__':
    n = int(input())
    student_marks = []
    # student_marks ={}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks.append([name,scores])
        # student_marks[name] = scores
    query_name = input()
    
    for name, scores in student_marks:
        if name==query_name:
            total=sum(scores)/3
    print(f"{total:.2f}")
    
    # sum=0
    # for i in student_marks[query_name]:
    #         sum=sum+i/3
    # print(f"{sum:.2f}")



