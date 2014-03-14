import pandas
import pandasql
import sys
import csv
import datetime

def reformat_subway_dates(date):
    '''
    The dates in our subway data are formatted in the format month-day-year.
    The dates in our weather underground data are formatted year-month-date.
    
    In order to join these two data sets together, we'll want the dates formatted
    the same way.  Write a function that takes as its input a date in the MTA Subway
    data format, and returns a date in the weather underground format.
    
    Hint: 
    There is a useful function in the datetime library called strptime. 
    More info can be seen here:
    http://docs.python.org/2/library/datetime.html#datetime.datetime.strptime
    '''
    
    theTimestamp = datetime.datetime.strptime(date, "%m-%d-%y")
    
    date_formatted = theTimestamp.strftime("%Y-%m-%d")
    
    return date_formatted

if __name__ == "__main__":

    # MTA formatted date: month-day-year
    theDate = '12-04-13'
    reformat_subway_dates(theDate) #result is a date in year-month-date
