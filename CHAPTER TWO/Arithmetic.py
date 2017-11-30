# Arithmetic Program
# This program will request the user to enter two numbers and the program will prints the sum, product, diffrence and quotient of the numbers 

#prompts the user to enter the first number
number1 = int(input('Enter the first number: ')) 

#prompts the user to enter the second number
number2 = int(input('\nEnter the second number: ')) 

#add the two numbers
sum = number1 + number2 

#the difference between the two numbers
difference = number1 - number2 

#product of the two numbers
product = number1 * number2  

#quotient of the two numbers
quotient = number1 / number2 

 #print the sum
print('\nThe sum of %d and %d is: %d' % (number1, number2, sum))

#print the difference
print('\nThe difference between %d and %d is: %d' % (number1, number2, difference))

#print the product 
print('\nThe product of %d and %d is: %d' % (number1, number2, product)) 

#print the quotient
print('\nThe quotient of %d and %d is: %d' % (number1, number2, quotient))
