t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # has_even = any(x % 2 == 0 for x in a)
    # has_odd = any(x % 2 == 1 for x in a)
    has_even=False
    has_odd=False
    for i in a:
        if i%2==0:
            has_even=True
        else:
            has_odd=True
            
    
    if has_even and has_odd:
        print(*sorted(a))
        # print(f"{has_even}--{has_odd}")
    else:
        print(*a)




