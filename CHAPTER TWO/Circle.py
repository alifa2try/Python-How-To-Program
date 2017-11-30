# Write a program that reads in the radius of a circle and prints the circle’s diameter, circumference and area. 
# Use the constant value 3.14159 for π. Do these calculations in output statements.

radius = float(input('Enter the radius of the circle: ')) #accepts the radius of the circle

print('\nThe diameter of the circle: %.2f' % (2 * radius )) #calculates and output the diameter
print('\nThe circumference of the circle: %.2f' % (2 * 3.14159 * radius )) #calculates and output the circumference
print('\nThe area of the circle: %.2f' % (3.14159 * radius ** 2)) #calculates and output the area