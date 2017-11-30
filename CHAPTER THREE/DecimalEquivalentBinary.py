# Decimal equivalent of binary number

'''
Input an integer containing 0s and 1s (i.e., a “binary” integer) and print its decimal equivalent.
Appendix C, Number Systems, discusses the binary number system. (Hint: Use the modulus and
division operators to pick off the “binary” number’s digits one at a time from right to left. Just as in
the decimal number system, where the rightmost digit has the positional value 1 and the next digit
leftward has the positional value 10, then 100, then 1000, etc., in the binary number system, the rightmost
digit has a positional value 1, the next digit leftward has the positional value 2, then 4, then 8,
etc. Thus, the decimal number 234 can be interpreted as 2 * 100 + 3 * 10 + 4 * 1. The decimal equivalent
of binary 1101 is 1 * 8 + 1 * 4 + 0 * 2 + 1 * 1.)
'''

highBit = 16 # value of highest bit
decimal = 0 # current value of decimal number
factor = 10000 # factor of 10 to pick up digits

#prompt for binary input
binary = int(input('Enter a binary number( 5 digit maximum): '))

number = binary #save in number for final display

while ( highBit >= 1 ):
    
    # update decimal value with decimal value corresponding to current highest binary bit 
    decimal += binary / factor  * highBit

    # reduce high bit by factor of 2, i.e., move one bit to the right 
    highBit /= 2

    #reduce binary number to eliminate current highest bit
    binary %= factor

    #reduce factor by power of 10, i.e., move one bit to the right 
    factor /= 10

print('The decimal equivalent of %d is %d\n' % (number, decimal))