# Palindrome Program
# Exercise 3.4 Deitel How To Program

'''
A palindrome is a number or a text phrase that reads the same backwards or forwards. For
example, each of the following five-digit integers is a palindrome: 12321, 55555, 45554 and 11611.
Write a program that reads in a five-digit integer and determines whether it is a palindrome. (Hint:
Use the division and modulus operators to separate the number into its individual digits.)
'''

number = int(input("Enter a five digit number: "))

temp1 = number

#determine the first digit by integer division by 10000
firstDigit = temp1 // 10000
temp2 = temp1 % 10000

#determine the second digit by integer division by 1000
secondDigit = temp2 // 1000
temp1 = temp2 % 1000

temp2 = temp1 % 100

#determine the fourth digit by integer division by 10
fourthDigit = temp2 // 10
temp1 = temp2 % 10


fifthDigit = temp1

if ( firstDigit == fifthDigit ):
    
    if ( secondDigit == fourthDigit ):
        print('%d is a palindrome\n' % number)
    else:
        print('%d is not a palindrome' % number)
else:
    print('%d is not a palindrome' % number)