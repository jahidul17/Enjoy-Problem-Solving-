T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    res = []
    for i in range(N):
        for j in range(i, N):
            res.append(max(A[i:j+1]))
    print(*res)

#This program given test case has issue.
