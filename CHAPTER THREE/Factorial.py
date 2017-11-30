# Factorial Program
# Part A: Write a program that reads a nonnegative integer and computes and prints its factorial.
# Exercise 3.6, Deitel Python How To Program

number = -1
factorial = 1

# loop until a valid input
while number < 0:
    number = int(input('Enter a positive integer: '))

n = number

# compute factorial
while ( n >= 0 ):
    
    if ( n == 0 ):
        factorial *= 1
    else:
        factorial *= n

    n -= 1

print('%d! is %d\n' % (number, factorial) )