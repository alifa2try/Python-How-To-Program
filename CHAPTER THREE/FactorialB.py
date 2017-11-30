# Factorial Part B
# Exercise 3.6b, Deitel Python How To Program

n = 0 # loop counter for accuracy
fact = 1 # current n factorial
accuracy = 10 # degree of accuracy
e = 0 # current estimated value of e

while ( n <= accuracy ):

    if( n == 0 ):
        fact *= 1
    else:
        fact *= n
  
    e += 1.0 / fact
    n +=1

print('e is %f\n' % e ) #display estimated value