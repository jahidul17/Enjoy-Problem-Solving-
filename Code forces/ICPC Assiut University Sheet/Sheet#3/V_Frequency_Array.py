# It accepet but show TLE error on codeforces

# n,m=map(int, input().split())

# lis=list(map(int, input().split()))

# for i  in range(1,m+1):
#     val=lis.count(i)
#     print(val)
    
    
    
# ----------------It's form Gemini and accept ----------------------

import sys

# Fast reading of input is crucial for large N and M
# Read N and M
try:
    N, M = map(int, sys.stdin.readline().split())
except Exception:
    sys.exit()

# Read the array A
try:
    A = list(map(int, sys.stdin.readline().split()))
except Exception:
    A = []

# 1. Initialize Frequency Array (O(M) time)
# We create a list of size M+1, initialized to zero, for 1-based indexing.
frequency = [0] * (M + 1)

# 2. Count Frequencies (O(N) time)
# Iterate through the input array A once.
for num in A:
    # Since the problem guarantees 1 <= A[i] <= M, 
    # we can use 'num' directly as the index.
    if 1 <= num <= M:
        frequency[num] += 1

# 3. Print Results (O(M) time)
# Iterate from 1 to M and print the stored count.
for i in range(1, M + 1):
    print(frequency[i])