
s=input()

for i in range(len(s)):
    if (s[i]=="\\"):
        break
    else:
        print(s[i],end="")

