'''
Author: Faisal Ali Garba, 
Exercise 3.8: Pythogorean Triples, Python Deitel How To Program
'''

count = 0 # number of triples found

# side1 values ranges from 1 to 500
for side1 in range( 1, 501 ):
    
    # side2 values ranges from current side1 to 500
    for side2 in range( 1, 501 ):
        
        # hypotenuse values ranges from current side2 to 500 
        for hypotenuse in range( 1, 501 ):
            
            hyptSquared = hypotenuse * hypotenuse
            sideSquared = side1 * side1 + side2 * side2
            
            if ( hyptSquared == sideSquared ):
                
                # display triple
                print( '%d %d %d\n' % (side1, side2, hypotenuse) )
                count += 1

# display a total number of triples found.
print( 'A total of %d triples were found. \n' % count )    