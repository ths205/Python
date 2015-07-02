#This progran purpose is to normalise the spaces in the row with the headline bio


import csv

with open('test.csv') as csvfile:

    #reads the file
    reader= csv.DictReader(csvfile)

    #opens file to write to
    with open('solutions.csv', 'w') as wte:
        #adds bio as a header
        fieldname=['bio']
        writer=csv.DictWriter(wte,fieldnames=fieldname, delimiter=' ')

        writer.writeheader()

        #loops through the file
        for row in reader:

            #print(" ".join(row['bio'].split()))
            #normalizes space
            writer.writerow({'bio':" ".join(row['bio'].split())})
