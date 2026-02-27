# def can_win(s):
#     s = list(s)
#     n = len(s)
    
#     while True:
#         made_move = False
        
#         # Try to find a valid pair (i, j)
#         for i in range(n):
#             if s[i] == '*':
#                 continue
#             for j in range(i+1, n):
#                 if s[j] != s[i]:
#                     continue
#                 # check if all middle elements are '*'
#                 if all(s[k] == '*' for k in range(i+1, j)):
#                     # valid move found, remove pair
#                     s[i] = '*'
#                     s[j] = '*'
#                     made_move = True
#                     break
#             if made_move:
#                 break
        
#         if not made_move:
#             break
    
#     # check if all are '*'
#     return all(ch == '*' for ch in s)

# # -------------------------------
# # Input & Output
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     s = input().strip()
    
#     if can_win(s):
#         print("YES")
#     else:
#         print("NO")