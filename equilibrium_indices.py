#An equilibrium index of this array is any integer P such that 0 <= P< N
#and the sum of elements of lower indices is equal to the sum of higher
#indices
#An array consisting of 8 elements A=[-1,3,-4,5,1,-6,2,1]

#P=1 is an equilibrium index of this array since A[0]=-1=A[2]+A[3]+A[4]+A[5]+A[6]

M=[-1,3,-4,5,1,-6,2,1]

def solution(A):
    for i in range(0,len(A)):
        if i==0 or i==len(A)-1:
            #if A[1]+A[2]+A[3]+A[4]+A[5]+A[6]+A[7]:
             if sum(A[:i])==0:
                print i

        elif i > 0 and i < len(A)-1:
             if sum(A[:i])==sum(A[i+1:]):
                print i

        #elif  i==len(A)-1:

             #if sum(A[:i])==0:
                #print i-1

        else:
                print -1

print(solution(M))
