#This program will use the Babylonian square-root algorithm and
#recursion to find square roots of any positive number



def babylonian_find_square_root(x_0,s, decimal_places):

#Checks to make sure the initial guess is not a zero
    if x_0 ==0:
       raise ZeroDivisionError('You entered a zero as your initial guess please enter a positive number')
        
#Checks that the user does not enter strings or characters as data
if type(x_0)==str or type(x_0)==chr or type(s)==str or type(s)==chr or type(decimal_places)==str or type(decimal_places)==chr:
       raise TypeError('You entered either string or char as data for initial guess, root or decimal places please enter numbers')    

#Checks to make sure the input is not negative
    if x_0 < 0 or s< 0 or decimal_places < 0:
       raise ValueError('You entered data that is negative.Please enter a positive number to get the square root of, enter a positive number as an initial guess, and as number of decimal places')


    x_new = float((x_0 +( s / x_0 ) )/2)

    if abs(x_0 - x_new)  < (pow(10,-decimal_places)) :
       return x_new

    return babylonian_find_square_root(x_new,s,decimal_places)

#Checks that the user does not put in data that cannot be converted to floats
try:

    s=input('Please enter a positive number that you wish to get the square root of')

    x_initial_guess=input('Please enter a positive number as a guess')

    decimal_places = input('Please enter how decimal places do you want the square root solution to be rounded to ')
    print( babylonian_find_square_root(float(x_initial_guess),float(s),int(decimal_places) ) )

except ValueError:

    print("You entered data that is not an integer, double or float")
    exit()
