#This program is to calculate the subfactorial using the formula
# !n = n * !(n-1)  + (-1)^(n)

def factorial_sub(n):
    if type(n)  !=  int:
       raise TypeError('You did not enter an integer')

    if n < 1:
       raise ValueError('You entered  either  0  or a  negative number')

    if n ==1:
       return 0

    if n==2:
       return 1



    return n * factorial_sub(n-1) + pow(-1,n)

try:
    
    #print(factorial_sub(6))
    #print(factorial_sub(4))
    y=int(input('Please enter a positive integer'))
    print(factorial_sub(y))

except ValueError:

    print("You did not enter valid data that can be converted to an integer")
    exit()

