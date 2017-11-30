'''
PerfectNumbers Program
Author: Faisal Ali Garba ( Malware Analyst ), Date: 29/11/2017

An integer number is said to be a perfect number if the sum of its factors, including 1 (but not the number itself),
is equal to the number. For example, 6 is a perfect number, because 6 = 1 + 2 + 3. Write a function perfect that 
determines whether parameter number is a perfect number. Use this function in a program that determines and prints all
the perfect numbers between 1 and 1000. Print the factors of each perfect number to confirm that the number is indeed
perfect. Challenge the power of your computer by testing numbers much larger than 1000
'''

def isPerfectNumber( num ):
    
    sum = 0
 
    for i in range( 1, num ):
        if num % i == 0:
            sum += i
    
    if sum == num:
        return 1 
    else:
        return 0

for j in range( 1, 2001 ):
    if( isPerfectNumber( j ) ):
        print( '%d is a perfect number' % j )
