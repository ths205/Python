import date_simple as ds
from datetime import date



def main():

    print(ds.get_date('2016-05-05'))
    print(ds.get_date('5/5/2016'))
    print(ds.get_date('5-May-16'))

    print(ds.format_date(date(2016,5,5)))
    print(ds.format_date(date(2016,5,5),'MM/DD/YYYY'))
    print(ds.format_date(date(2016,5,5),'DD-Mon-YY'))
