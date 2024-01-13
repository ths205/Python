
#This program returns whether an integer is a perfect square or not.

def perfect_square(x):


     if type(x) != int:

        raise TypeError('Please  enter a  positive integer')

     if x < 0:
        raise ValueError('Please enter a number greater than 0')
     if x==0:
        return "It is a perfect square"  

     for i in range(1, x+1):

         if x/i == i:
            return "It is a perfect square"

         else:

            continue

     return "It is not a perfect square"


#print(perfect_square(100))
#The try except will catch invalid data that cannot be coverted to an int
try:
     number =  int(input("Please Enter a Postive number"))



     print(perfect_square(number))

except ValueError:

     print("You did not enter input that can be converted to an integer")
     exit()
