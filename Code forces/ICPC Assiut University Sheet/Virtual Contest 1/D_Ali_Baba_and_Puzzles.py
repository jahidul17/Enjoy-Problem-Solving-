a, b, c, d = map(int, input().split())

if ((a + b) + c == d or
    (a + b) - c == d or
    (a + b) * c == d or
    (a - b) + c == d or
    (a - b) - c == d or
    (a - b) * c == d or
    (a * b) + c == d or
    (a * b) - c == d or
    (a * b) * c == d or
    a + (b + c) == d or
    a + (b - c) == d or
    a + (b * c) == d or
    a - (b + c) == d or
    a - (b - c) == d or
    a - (b * c) == d or
    a * (b + c) == d or
    a * (b - c) == d or
    a * (b * c) == d):
    print("YES")
else:
    print("NO")



# a,b,c,d=map(int, input().split())

# if(a+b+c==d):
#     print("YES")
# elif(a+b-c==d):
#     print("YES")
# elif(a+b*c==d):
#     print("YES")
# elif(a*b*c==d):
#     print("YES")
# elif(a*b+c==d):
#     print("YES")
# elif(a*b-c==d):
#     print("YES")
# elif(a-b-c==d):
#     print("YES")
# elif(a-b+c==d):
#     print("YES")
# elif(a-b*c==d):
#     print("YES")
# else:
#     print("NO")


