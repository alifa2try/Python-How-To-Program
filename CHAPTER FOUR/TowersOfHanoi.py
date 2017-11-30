'''
Author: Faisal Ali Garba ( Malware Analyst ), Date: 30/11/2017
Towers of Hanoi Program
Exercise 4.8: Python How To Program, Deitel
'''

# tower recursively prints instructions for moving disks from start peg to end peg using temp peg for temporary storage
def tower( c, start, end, temp ):
    
    # base case 
    if( c == 1 ):
        print( '%d --> %d\n' % ( start, end ) )
        return
    #end if	

    # move c - 1 disks from start to temp
    tower( c - 1, start, temp, end )

    # move last disk from start to end
    print( '%d --> %d\n' % ( start, end ) )
    
    # move c - 1 disks from temp to end  
    tower( c - 1, temp, end, start )
# end function tower

n = int( input( 'Enter the starting number of disks: ' ) )

# print instructions for moving disks from peg 1 to peg 3 using peg 2 for temporary storage
tower( n, 1, 3, 2 )