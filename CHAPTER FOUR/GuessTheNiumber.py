'''
Author: Faisal Ali Garba ( Malware Analyst ), Date: 29/11/2017
Exercise 4.7: Python How To Program by Deitel
'''

from random import randint, seed # import randint and seed functions
from datetime import datetime  # import datetime
seed( datetime.now() ) # seed the random generator with the current date's time   


def guessGame():
    response = 1
    while( response == 1 ):
        x = randint( 1, 1000 )
        print( '\nI have a number in the range 1 and 1000\n' )
        print( 'Can you guess my number?\n' )
        print( 'Please type your first guess.\n' )
        guess = int( input( 'guess: ') )

        while( guess != x ):

            if ( guess < x ):
                print( 'Too low. Try again.\n' )
            else:
                print( 'Too high. Try again.\n' )

            guess = int( input( 'guess: ' ) )
    
        print( '\nExcellent! You guessed the number again!\n')
        print( 'Would you like to play again?\n' )
        print( 'Please type ( 1 = yes, 2 = no )?' )
        response = int( input( 'response: ' )) 

guessGame()