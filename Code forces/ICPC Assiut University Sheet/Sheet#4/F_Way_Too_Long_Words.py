t=int(input())

for _ in range(t):
    string=input()
    digit=len(string)
    if(digit>10):
        print(f"{string[0]}{digit-2}{string[-1:]}")
    else:
        print(string)


