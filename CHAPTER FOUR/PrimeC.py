'''
Author: Faisal Ali Garba( Malware Analyst ), Date: 29/11/2017
Exercise 4.4: Prime Program, Python How To Program by Deitel

An integer greater than 1 is said to be prime if it is divisible by only 1 and itself. For example, 2, 3, 5 and 7 are
prime numbers, but 4, 6, 8 and 9 are not.
a) Write a function that determines whether a number is prime.
b) Use this function in a program that determines and prints all the prime numbers between 2 and 1,000. 
c) Initially, you might think that n/2 is the upper limit for which you must test to see whether a number is prime, 
but you need go only as high as the square root of n. Rewrite the program and run it both ways to show that you get 
the same result.
'''
import math

def isPrime( num ):
    
    numSquare = math.sqrt( num ) 

    if numSquare % 2 == 0:
        print( '%d\t' % num, end = '' )

for number in range( 2, 1000 ):
    isPrime( number )

    if number % 10 == 0:
        print( )