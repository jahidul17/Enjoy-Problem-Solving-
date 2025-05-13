n=int(input())
hour=n//3600
n=n%3600
minute=n//60
n=n%60

print(f"{hour}:{minute}:{n}")
