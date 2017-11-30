'''
Author: Faisal Ali Garba ( Malware Analyst ), Date: 29/11/2017
CAI2: The use of computers in education is referred to as computer-assisted instruction (CAI). One problem that 
develops in CAI environments is student fatigue. This can be eliminated by varying the computer's dialogue to hold the
student's attention. Modify the program of Exercise 5.32 so the various comments are printed for each correct answer 
and each incorrect answer as follows:

Responses to a correct answer

Very good!
Excellent!
Nice work!
Keep up the good work!

Responses to an incorrect answer

No. Please try again.
Wrong. Try once more.
Don't give up!
No. Keep trying.

Use the random number generator to choose a number from 1 to 4 to select an appropriate response to each answer. Use a
switch statement with printf statements to issue the responses.
'''

from random import randint, seed # import randint and seed functions
from datetime import datetime  # import datetime
seed( datetime.now() ) # seed the random generator with the current date's time   

def multiplication():

    response = 0
    right = 0.0
    wrong = 0.0
    
    for count in range( 1, 11 ):
        x = randint( 1, 9 ) # generates 1 digit random number
        y = randint( 1, 9 )	#  generates 1 digit random number

        print( 'How much is %s times %s?' % ( str( x ), str( y ) ) )
        response = int( input( 'Response: ' ) )

        # loop while not sentinel value or correct response from user
        while ( response != x * y ):
            wrong += 1.0
            incorrectMessage()
            response = int( input( 'Response: ' ) )

        right += 1.0 
        correctMessage()

    if ( float(right) / float(right + wrong) < 0.75 ):
        print( 'Please ask your instructor for extra help.\n' )

def correctMessage():
    a = randint( 1, 4 )
    
    if ( a == 1 ):
        print( 'Very good!\n\n' )
    elif( a == 2 ):
        print( 'Excellent!\n\n' )
    elif( a == 3 ):
        print( 'Nice work!\n\n' )
    elif( a == 4 ):
        print( 'Keep up the good work!\n\n' )
    else:
        print( 'How comes you reach this line?' )

def incorrectMessage():
    a = randint( 1, 4 )
    
    if ( a == 1 ):
        print( 'Nope. Please try again\n\n' )
    elif( a == 2 ):
        print( 'Wrong. Try once more\n\n' )
    elif( a == 3 ):
        print( "Don't give up!\n\n" )
    elif( a == 4 ):
        print( 'No. Keep trying!\n\n' )
    else:
        print( 'How comes you reach this line?' )

multiplication()