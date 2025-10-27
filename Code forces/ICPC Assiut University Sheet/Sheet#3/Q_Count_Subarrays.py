T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    count = 1  # single element subarray
    length = 1
    
    for i in range(1, N):
        if A[i] >= A[i - 1]:
            # print(A[i],A[i-1])
            length += 1
            # print(f"Inner{A[i]}")
        else:
            length = 1
            # print(f"Outer{A[i]}")
        count += length
        # print(count)
    
    print(count)
