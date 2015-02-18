import random

#This program is to randomly pick a letter from the dna sequence\
#Then replace the letter with another randomly picked letter.

#this is the dna sequence

dna="ACTCTGTGAATTTGAGGGCAGTATGCGTGATACTTTAGAGAAACTGTTGTCTGGACC\
CCCCGTCACCACTGTCTACGCAACCAGCAATTGTCACTTAGGTTACGTCTTAGCCG\
ACCTAGTTCAATGTAAGTTGGTAGAAC\n"

print"Before Substitution"

print " "

print dna

#picks a random letter from the dna sequence
pick_letter=random.randint(0, len(dna)-1)

#picks a different random letter to substitute the pick_letter variable
sub_letter=random.randint(0, len(dna)-1)

#checks to make sure the letter picked is no being replaced
#by the same letter
if dna[pick_letter]== dna[sub_letter]:
    
    sub=random.randint(0, len(dna))





dna=dna[0:pick_letter]+dna[sub_letter]+dna[pick_letter+1:]

print "After Substitution"
print "  "
print dna
