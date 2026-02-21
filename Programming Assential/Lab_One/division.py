num1=input('Enter first number: ')
num2=input('Enter second number: ')
division=float(num1)/float(num2) #Type casting
# print('The result is = ',int(division))
print('The result is = %.2f'%division)
print('The result is = %.2f and Then %.4f'%(division,division+3)) #print specific decimal point