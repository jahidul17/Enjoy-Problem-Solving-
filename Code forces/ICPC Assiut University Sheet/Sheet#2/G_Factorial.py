# n=int(input())
# try:
#     while n:
#         fact =1
#         x=int(input())
#         for i in range(1,x+1):
#             fact=fact*i
#         print(fact)
# except:
#     exit()



#simple way
# Step 1: Read the number of test cases
T = int(input())  

# Step 2: Process each test case
# for g in range(T):
for _ in range(T): #The underscore (_) is used as a loop variable when we don't actually need its value. It's a common Python convention to indicate that the loop variable is unused.
    N = int(input())  # Read the number
    
    # Step 3: Calculate factorial without using built-in function
    factorial = 1
    for i in range(1, N + 1):
        factorial *= i
    
    # Step 4: Print the factorial of N
    print(factorial)

