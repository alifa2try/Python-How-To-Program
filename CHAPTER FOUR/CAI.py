'''
Author: Faisal Ali Garba( Malware Analyst ), Date: 29/11/2017
Exercise 4.6: CAI

Computers are playing an increasing role in education. The use of computers in education is referred to as 
computer-assisted instruction (CAI). Write a program that will help an elementary school student learn multiplication. Use the random module to produce two positive one-digit integers.
The program should then display a question, such as:
 
''How much is 6 times 7?''

The student then types the answer. Next, the program checks the student’s answer. If it is correct, print the string
"Very good!" on the screen and ask another multiplication question. If the answer is wrong, display "No. Please try
again." and let the student try the same question again repeatedly until the student finally gets it right. A separate
function should be used to generate each new question. This method should be called once when the program begins
execution and each time the user answers the question correctly. (Hint: To convert the numbers for the problem into
strings for the question, use function str. For example, str( 7 ) returns "7".) 
'''

from random import randint, seed # import randint and seed functions
from datetime import datetime  # import datetime
seed( datetime.now() ) # seed the random generator with the current date's time   

def multiplication():

    response = 0

    print( 'Enter -1 to end.\n' )

    # loop while sentinel value not read from user
    while ( response != -1 ):
        x = randint( 1, 9 ) # generates 1 digit random number
        y = randint( 1, 9 )	#  generates 1 digit random number

        print( 'How much is %s times %s?' % ( str( x ), str( y ) ) )
        response = int( input( 'Response: ' ) )

        # loop while not sentinel value or correct response from user
        while ( response != -1 and response != x * y ):
            print( 'Nope. Please try again! \n' )
            response = int( input( 'Response: ' ) )

        if ( response != -1 ): 
            print( 'Very good!\n\n' )

    print( 'That is all for now, bye.\n' )

multiplication()