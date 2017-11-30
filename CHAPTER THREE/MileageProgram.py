# Mileage Program
# Exercise 3.3 Deitel Python How To Program

totalGallons = 0.0
totalMiles = 0.0

gallons = float(input('Enter the gallons used (-1 to end):'))

while ( gallons != -1.0 ):
    totalGallons += gallons

    miles = float( input('Enter the miles driven: ' ))
    totalMiles += miles

    print('The miles / gallon for this tank was %.2f\n\n' % (miles/gallons))

    gallons = float(input('Enter the gallons used (-1 to end):'))

totalAverage = totalMiles / totalGallons

print('\nThe overall average Miles/Gallons was %.2f\n' % totalAverage)