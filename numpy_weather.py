"""
This program is to get the Weather data from the Chicago, New York, and Los Angelas csv files and
calculate mean, max, min and standard deviation using version Python 2.7 and numpy. The user would have to
put in losangelas, newyork, honolulu or chicago at the command line in order to get the data of a specific csv file.
Problem 1.1
"""

import numpy as np

import csv
"""Helps the program get an argument from the user in the command line"""
import sys



"""Gets the second argument from the input that the user has put in in the command line"""
y = sys.argv[1]

"""The try error checks if the file exists based on the argument
   the user puts in from the command line."""

try:

    data_directory = 'weather_files/weather_'+y+'.csv'

    with open(data_directory) as csvfile:

        read_rows = csv.DictReader(csvfile)

        mean_temp_f = []

        for row in read_rows:

            #print(row)
            mean_temp_f.append( int( row['Mean TemperatureF'] ) )

        A = np.array(mean_temp_f)
        #average using numpy
        avg = np.mean(A)
        
        #maximum value using numpy
        max_temp = np.amax(A)
        
        #minimum value using numpy
        min_temp = np.amin(A)

        #standard deviation with numpy

        sd = np.std(A)
        
        print 'Average temp : ' + str(avg )

        print 'Max temp: ' + str( max_temp )

        print 'Min temp: ' + str( min_temp )

        print 'Standard_deviation: ' + str( sd)

except IOError:

    print 'The File is not found'
    exit()
