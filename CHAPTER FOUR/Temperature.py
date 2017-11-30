'''
Author: Faisal Ali Garba ( Malware Analyst ), Date: 29/11/2017
Exercise 4.3: Temperature Program  from Python How To Pogram by Deitel

Implement the following function fahrenheit to return the Fahrenheit equivalent of a Celsius temperature.
F = (9/5) * C + 32
Use this function to write a program that prints a chart showing the Fahrenheit equivalents of all Celsius temperatures
0–100 degrees. Use one position of precision to the right of the decimal point for the results. Print the outputs in 
a neat tabular format that minimizes the number of lines of output while remaining readable.
'''

def fahrenheit( cel ):
    fah = ( 9 / 5 ) * cel + 32
    
    return fah

# display table of fahrenheit equivalent of Celsius temperature
print( 'Fahrenheit equivalent of Celsius temperature:\n' )
print( 'Celsius\t\tFahrenheit' )

# display fahrenheit equivalent of Celsius 0 to 100
for celcius in range( 101 ):
    print( '%d\t\t%d\n' % ( celcius, fahrenheit( celcius ) ) )