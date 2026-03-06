n=int(input('Enter a number of summation range: '))

if( n>0):
    sum=0
    while(n>0):
        sum+=n
        n=n-1
    print('The summation of n is = ',sum)
     
else:
    print('Enter a positive number.')
        
    
