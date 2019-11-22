"""
Tiffany Schiff
This program helps convert strings to dates or dates to strings
using Python 2.7
"""

from datetime import date

def get_date(x):

    """This function takes an optional string and returns a date object."""
    if type(x) != str:

       raise TypeError('You need to enter a type string')

    #d_year = x[0:4]
    #d_month = x[5:7]
    #d_day = x[8:10]



    elif x[4] == '-' and x[7] == '-':

         """This elif checks for the format YYYY-MM-DD"""

         d_split=x.split('-')



         d_year = int(d_split[0])
         d_month = int(d_split[1])
         d_day = int(d_split[2])
         
    if d_month > 12 or d_month <1:

             raise ValueError('You did not put in a value for month between 1 and 12')

         if d_year < 0 or d_day < 0:

             raise ValueError('You did not put in a positive value for year or day')



         d = date(d_year, d_month, d_day)



    elif x[1] == '/' and x[3] == '/':

         d_split = x.split('/')

         d_month = int(d_split[0])

         d_day = int(d_split[1])

         d_year = int(d_split[2])

         if d_month > 12 or d_month <1:

             raise ValueError('You did not put in a value for month between 1 and 12')

         if d_year < 0 or d_day < 0:

             raise ValueError('You did not put in a positive value for year or day')

         d = date(d_year, d_month, d_day) 
         
         elif x[1] == '/' and x[3] == '/':

         d_split = x.split('/')

         d_month = int(d_split[0])

         d_day = int(d_split[1])

         d_year = int(d_split[2])

         if d_month > 12 or d_month <1:

             raise ValueError('You did not put in a value for month between 1 and 12')

         if d_year < 0 or d_day < 0:

             raise ValueError('You did not put in a positive value for year or day')
             
         elif x[1] == '-':

         """This elif checks for the format D-M-Y"""

         d_split = x.split('-')

         d_day = int(d_split[0])

         d_month = d_split[1]

         d_year = int(d_split[2])

         mydict={'January': 1,
                 'February': 2,
                 'March': 3,
                 'April': 4,
                 'May': 5,
                 'June': 6,
                 'July': 7,
                 'August': 8,
                 'September':9,
                 'October': 10,
                 'November': 11,
                 'December': 12

                }

         for key in mydict.keys():

             if d_month == key:

                d_month_int = mydict[key]
                break



         if d_year < 0 or d_day < 0:

             raise ValueError('You did not put in a positive value for year or day')

         d = date(d_year, d_month_int, d_day)

    return d

def add_day(v, s=0):

    """This function adds a day to the date"""

    if type(v) != date:

       raise TypeError('You need to enter an object of type date')

    if v.day < 0:

       raise ValueError('You need to enter a positive iinteger for day')

    return date(v.year, v.month, v.day + s)

 def add_week(yr, d=0):

    """This function adds the number of weeks."""
    week = d*7

    return date(yr.year, yr.month, yr.day + week)
    
 def format_date(u,z=''):
    

    """Takes a date object and optional string and returns a string"""

    if type(u) != date:
       raise TypeError('You did not enter a parameter of type date')

    if z == '':

       date_str = u.isoformat()

    

    elif z =='MM/DD/YYYY':

       yr = str(u.year) #gets the string for year
       m = str(u.month) #gets the string for month
       d = str(u.day) #gets the string for day

       g = u.month
       h =u.day
       
     """checks if the month is less than 10
       if g < 10:

           date_str ='0'+ m +'/'+d+'/'+'/'+yr

       ""checks if day is less than 10"""
       if h < 10:

           date_str =m +'/'+'0'+d+'/'+'/'+yr

       """checks if both month and day are less than 10"""
       if g < 10 and h < 10:


           date_str ='0'+m +'/'+'0'+d+'/'+yr

    elif z =='DD-Mon-YY':

       my_dict_2={1:'January',
                 2:'February',
                 3:'March',
                 4:'April',
                 5:'May',
                 6:'June',
                 7:'July',
                 8:'August',
                 9:'September',
                 10:'October',
                 11:'November',
                 12:'December'

                }
                
                g = u.month
       h = u.day
       y = u.year

       y_s = str(y)
       for key in my_dict_2.keys():

           if key == g:

               g = my_dict_2[key]
               break

       if h < 10:

           date_str = '0' + str(h)+ '-' + g +'-'+ y_s[2:4]

    elif z !='DD-Mon-YY' or z != 'MM/DD/YYYY':
       raise ValueError('You did not enter a parameter with the format MM/DD/YYYY or DD-Mon-YY')



    return date_str
