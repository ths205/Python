        #This file calculates x to the power n


def x_to_pow_n(x,n):
    if type(n)==str or type(x)==str or type(n)==bool or type(x)==bool:
       raise TypeError('Please enter a float, double or integer for x and a float double or integer as an exponent')
    if x==0 and n<0:
       raise ZeroDivisionError('You gave me a number x which is 0 and an exponent that is less than 0')


    if n==0:
       return 1

    if n<0:
       return 1.0/(x*x_to_pow_n(x,(-n)-1))


    return x*x_to_pow_n(x,n-1)


print(x_to_pow_n(3,3))
print(x_to_pow_n(3.4,3))
print(x_to_pow_n(2,-2))
#print(x_to_pow_n(0,-2))
print("%.4f" % x_to_pow_n(3,-2))
#print(x_to_pow_n(3,"yes"))
