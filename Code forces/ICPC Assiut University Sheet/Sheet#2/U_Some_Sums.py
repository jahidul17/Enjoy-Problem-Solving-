n,a,b=map(int,input().split())
sum=0
for i in range(n+1):
    # digits_list = [int(digit) for digit in str(i)]

    # sumDigit=0
    # for j in digits_list:
    #     sumDigit+=j
    # print(sumDigit)
    
    #anotherway
    # --------
    rem=i
    sumDigit=0
    while(rem>0):
        div=rem%10
        rem=rem//10
        sumDigit+=div
    # print(sumDigit)
    # --------
    
    if(sumDigit>=a and sumDigit<=b):
        sum+=i
print(sum)

# print(digits_list)
# print(n,a,b)


"""
Step-by-Step Explanation with an Example
Let's use the provided example: N = 20, A = 2, B = 5.

Initialize a sum variable: Create a variable, let's call it total_sum, and set it to 0.

Iterate from 1 to 20: The loop will check each number from 1 up to 20.

Number	Sum of Digits	Condition (2 ≤ sum ≤ 5)	Action	total_sum
1	1	No	Skip	0
2	2	Yes	Add 2	2
3	3	Yes	Add 3	5
4	4	Yes	Add 4	9
5	5	Yes	Add 5	14
6	6	No	Skip	14
...	...	...	...	...
10	1+0=1	No	Skip	14
11	1+1=2	Yes	Add 11	25
12	1+2=3	Yes	Add 12	37
13	1+3=4	Yes	Add 13	50
14	1+4=5	Yes	Add 14	64
15	1+5=6	No	Skip	64
...	...	...	...	...
19	1+9=10	No	Skip	64
20	2+0=2	Yes	Add 20	84

"""