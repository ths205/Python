#This program converts a Roman numerals string and sums its letters to an integer

#y="MDCCLXXVI"

#z='XIV'

y=input('Enter a Roman Numeral')

roman_int_dict={"I":1,"V":5,"X":10,"L":50, "C":100, "D":500, "M":1000}

arabic_int=0

prev=""

for i in y:


    #produces 4 or 9 based on Roman Numerals IV and IX
    if ( prev=='I' and (i=='V' or i=='X'))  or ( prev=='C' and (i=='D' or i=='M')) or (prev=='X' and(i=="L" or i=="C")):

           arabic_int += roman_int_dict[i]-2*roman_int_dict[prev]
           continue



    for key in roman_int_dict.keys():




        if i==key:
           arabic_int += roman_int_dict[key]

    prev = i
print(arabic_int)
