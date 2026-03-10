# n=int(input())
# s=input()

# print("".join(sorted(s)))
# print(min(s))  // a 

# TLE would not  solve
import sys
n=int(sys.stdin.readline())
s=sys.stdin.readline().strip()
 
freq=[0]*26

for i in range(n):
    index=ord(s[i])-97
    freq[index]+=1
    
for i in range(26):
    for j in range(freq[i]):
        print(chr(i+97),end="")

