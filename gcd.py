
#This program is to find the gcd(Greatest Common Denominator) using the Euclidean Algorithm and recursion

def gcd(x,y):

    if type(x) != int:
       raise TypeError('You did not enter an integer for value x')

    if type(y) != int:
       raise TypeError('You did not enter an integer for value Y')

    if  x < 0:

       raise ValueError('You entered a negative number please enter zero or a positive number for x')

    if  y < 0:

       raise ValueError('You entered a negative number please enter zero or a positive number for y')


    if x==0 and y >= 0:
       return y

    if x>=0 and y==0:
       return x


    quotient = x / y

    remainder = x % y

    return gcd(y, remainder)



print(gcd(270,192))
