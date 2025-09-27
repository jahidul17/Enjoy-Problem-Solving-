# Read inputs
S = input().strip()             # symbol
N = int(input().strip())        # number count
numbers = list(map(int, input().split()))

# Print repeated symbols
for x in numbers:
    print(S * x)
