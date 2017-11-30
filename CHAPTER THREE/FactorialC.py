'''
Author: Faisal Ali Garba (Malware Analyst), Date 24/11/2017   
Exercise 3.6, Deitel How To Program
FactorialC
'''
 
n = 0 # counter
accuracy = 15 # degree of accuracy
x = 13 # exponent 
times = 0 # counter
e = 1.0 # e raised to the x power
exp = 0.0 # x raised to the n power
fact = 1.0 # factorial
count = 0 # copy of n

while ( n <= accuracy ):
    
    if( n == 0 ):
        fact *= 1.0
    else:
        fact *= n

    while ( times < count ):
        if ( times == 0 ):
            exp = 1.0
            exp *= x 
        else:
            exp *= x

        times += 1

    e += exp / fact
    n += 1

print('e raised to the %d power is %.2f\n' % ( x, e ) )