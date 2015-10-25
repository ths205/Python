#This program puts a table from a csv file into a database

import csv
 
with open('csv-data/car-set-1.csv') as csvfile:
 
 
     reader=csv.DictReader(csvfile)
 
     with open('icdb.db', 'w') as car_wte:
         fieldname=['year','make','model']
         #fieldname=['year']
         writer=csv.DictWriter(car_wte, fieldnames=fieldname, delimiter=' ')
 
         writer.writeheader()
 
         #fieldname_model=['model']
         #writer_model=csv.DictWriter(car_wte, fieldnames=fieldname_model, delimiter=' ') 
         #writer_model.writeheader()
         for row in reader:
             writer.writerow({'year':" ".join(row['year'].split()), 'make':" ".join(row['make'].split()), 'model':" ".join(row['model'].split())})
 
          
         fieldname=['primary key']
 
         writer=csv.DictWriter(csvfile, fieldnames=fieldname)
 
