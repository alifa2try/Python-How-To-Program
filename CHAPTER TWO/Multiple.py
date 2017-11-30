# Write a program that reads in two integers and determines and prints whether the first is multiple of the second. 
# (Hint: Use the modulus operator.)

number1 = int(input('Enter the first number: '))

number2 = int(input('\nEnter the second number: '))

#determines whether the first is a multiple of the second
if (number1 % number2) == 0:
    print('\n%d is a multiple of %d' % (number1, number2)) 
