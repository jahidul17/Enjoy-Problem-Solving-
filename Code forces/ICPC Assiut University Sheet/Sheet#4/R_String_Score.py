n=int(input())
# s=input()
# print(s)
# n = int(input())
s = list(input())

score =0
i=0

while i<len(s):
    if s[i]=='V':
        score+=5
        
    elif s[i]=='W':
        score +=2
        
    elif s[i]== 'X':
        score +=

# score = 0
# i = 0

# while i < len(s):
#     if s[i] == 'V':
#         score += 5

#     elif s[i] == 'W':
#         score += 2

#     elif s[i] == 'X':
#         # next character remove
#         if i + 1 < len(s):
#             s.pop(i + 1)

#     elif s[i] == 'Y':
#         # move next character to end
#         if i + 1 < len(s):
#             ch = s.pop(i + 1)
#             s.append(ch)

#     elif s[i] == 'Z':
#         # check next character
#         if i + 1 < len(s):
#             if s[i + 1] == 'V':
#                 score //= 5
#                 s.pop(i + 1)
#             elif s[i + 1] == 'W':
#                 score //= 2
#                 s.pop(i + 1)

#     i += 1

# print(score)

