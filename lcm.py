
#Computes The least common  multiple by multiplying two numbers
# and dividing them by the Greatest Common Denominator of both numbers

#imports the file  gcd.py
import gcd

#Method to compute the least common  multiple
def lcm(a, b):

    if type(a) != int:
       raise TypeError('You did not enter an integer for value a')

    if type(b) != int:
       raise TypeError('You did not enter an integer for value b')

    if  a < 0:

       raise ValueError('You entered a negative number please enter zero or a positive number for a')

    if  b < 0:

       raise ValueError('You entered a negative number please enter zero or a positive number for b')

    if a==0 or b==0:
      return 0

    return int((a*b)/gcd.gcd(a,b))

print(lcm(140,72))
