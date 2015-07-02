#This program replaces State Abbreviation with the full state name

import csv

#opens file to write to
with open('solutions2.csv', 'w') as csvfile:
      fieldname=['state']

      writer=csv.DictWriter(csvfile,fieldnames=fieldname)


   

      dict={
             "AL":"Alabama",
             "AK":"Alaska",
             "AZ":"Arizona",
             "AR":"Arkansas",
             "CA":"California",
             "CO":"Colorado",
             "CT":"Connecticut",
             "DE":"Delaware",
             "FL":"Florida",
             "GA":"Georgia",
             "HI":"Hawaii",
             "ID":"Idaho",
             "IL":"Illinois",
             "IN":"Indiana",
             "IA":"Iowa",
             "KS":"Kansas",
             "KY":"Kentucky",
             "LA":"Louisiana",
             "ME":"Maine",
             "MD":"Maryland",
             "MA":"Massachusetts",
             "MI":"Michigan",
             "MN":"Minnesota",
             "MS":"Mississippi",
             "MO":"Missouri",
             "MT":"Montana",
             "NE":"Nebraska",
             "NV":"Nevada",
             "NH":"New Hampshire",
             "NJ":"New Jersey",
             "NM":"New Mexico",
             "NY":"New York",
             "NC":"North Carolina",
             "ND":"North Dakota",
             "OH":"Ohio",
             "OK":"Oklahoma",
             "OR":"Oregon",
             "PA":"Pennsylvania",
             "RI":"Rhode Island",
             "SC":"South Carolina",
             "SD":"South Dakota",
             "TN":"Tennessee",
             "TX":"Texas",
             "UT":"Utah",
             "VT":"Vermont",
             "VA":"Virginia",
             "WA":"Washington",
             "WV":"West Virginia",
             "WI":"Wisconsin",
             "WY":"Wyoming"

            }

      writer.writeheader()
      for key in dict.keys():
           writer.writerow({'state':dict[key]}) 
