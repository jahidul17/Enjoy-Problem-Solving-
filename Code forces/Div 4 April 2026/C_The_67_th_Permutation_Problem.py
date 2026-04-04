#not solved

# import sys

# def solve():
#     input_data = sys.stdin.read().split()
#     if not input_data:
#         return
    
#     t = int(input_data[0])
#     pointer = 1
#     results = []
    
#     for _ in range(t):
#         n = int(input_data[pointer])
#         pointer += 1
        
#         permutation = []
#         small = 1
#         large = 3 * n
        
#         for i in range(n):
#             # Block: [smallest, second largest, largest]
#             permutation.append(small)
#             permutation.append(large - 1)
#             permutation.append(large)
            
#             small += 1
#             large -= 2
        
#         results.append(" ".join(map(str, permutation)))
    
#     print("\n".join(results))

# if __name__ == "__main__":
#     solve()
