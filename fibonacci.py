#sums of the fibonacci numbers
sum=0

space=input('enter a positive integer to store the number of spaces in an array')

print(space)

if space < 0:
    print('You did not enter a positive number.')
    

if space==1:
    print('The sum is 0.')
    

fib=[]


fib.append(0)
fib.append(1)
print fib[0]
print fib[1]
z=fib[0]+fib[1]
sum=z
for x in range(2,space):
    y=fib[x-1]+fib[x-2]
    fib.append(y)
    sum +=y
    



print "the sum of %d" %space
print "spaces" 
print "is %d" %sum
