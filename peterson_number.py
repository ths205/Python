#A Peterson Number is where the sum of the factorials of each digit
#of the number is equal to the number itself. This program will
#check if a number is a Peterson Number.

def factorial(n):

    if n==0 or n==1:
       return 1

    if n==2:
       return 2

    return n*factorial(n-1)

def peterson_num(d,n):
#checks to make sure the user puts in good input.
    if type(n) !=int:
       raise TypeError('You entered input that is not an integer.')
    if n < 0:
       raise ValueError('You entered an integer that is less than 0.')

    total_num_fact=0
    for i in range(0, len(d)):
       total_num_fact+=factorial(int(d[i]))

    if n==total_num_fact:
       return str(n) +" is a Peterson number."

    return str(n) +" is not a Peterson number."

#Checks to make sure the user puts apprpriate input
try:

    x=input('Please enter a positive number')
    #print("The factorial of 6 is"+ str(factorial(6)))

    #print("The factorial of "+str(x)+" is "+str(factorial(int(x))))

    #makes a number into a list that contains a string of numbers
    arr=list(str(x))

    #int is  used to convert a string integer into an integer.
    print(peterson_num(arr,int(x)))

except ValueError:
       print("You did not type in a positive integer.")
       exit()

