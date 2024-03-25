#This program returns whether an integer is an Alexandrian Integer or not

def alex_integer(a,p,q,r):
    
    if type(a) != int or  type(p) != int or  type(q) != int or  type(r) != int:
       raise TypeError('You gave input that is not an integer.PLease give a non-zero integer')

    if a==0 or p==0 or q==0 or r==0:
       raise ZeroDivisionError('You gave a zero integer. Please give a non-zero integer.')

    if a == p*q*r and round( float(1/a), 14)== round(float( 1/p +1/q +1/r), 14) :

       return str(a) + " is an Alexandrian Integer"
    #print(float( 1/p +1/q +1/r)  )
    #print(float(1/a))
    return str(a) + " is not an Alexandrian Integer"



print(alex_integer(6,3,2,1))
print(alex_integer(6,-3,-2,1))
print(alex_integer(630,5,-7,-18))
#print(alex_integer(6,-3,-2,0))
