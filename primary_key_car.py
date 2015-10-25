#This program appends a dictionary of primary keys to the table that car_evaluation.py put into the databse.

import csv 
 
with open('icdb.db', 'a') as csvfile:
    fieldname=['primary key']
     
    writer=csv.DictWriter(csvfile, fieldnames=fieldname)
 
    prime_k={"1":9919,
             "2":0123,
             "3":0321,
             "4":0214,
             "5":5719,
             "6":9157, 
             "7":6691,
             "8":9193, 
             "9":9091,
             "10":9020,
             "11":3519,
             "12":9661}
 
    writer.writeheader()
    for key in prime_k:
       writer.writerow({'primary key':prime_k[key]})
