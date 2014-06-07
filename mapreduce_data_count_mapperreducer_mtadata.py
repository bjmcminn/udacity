import logging
import sys
import string
import re

# Commented for debugging
#from util import logfile

#logging.basicConfig(filename=logfile, format='%(message)s',
                   #level=logging.INFO, filemode='w')


def mapper():

"""
    The input to this mapper will be the final Subway-MTA dataset, the same as
    in the previous exercise.  You can check out the csv and its structure below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

    For each line of input, the mapper output should
    1) return the UNIT as the key
    2) return the number of ENTRIESn_hourly as the value
    3) Separate the key and the value by a tab, for example:
       R002\t105105.0

    Since you are printing the actual output of your program, you
    can't print a debug statement without breaking the grader.
    Instead, you should use the logging module which we've configured
    for you.
    
    For example:
    logging.info("My debugging message")
    
    The logging module can be used to give you more control over your debugging
    or other messages than you can get by printing them.  In this exercise, print
    statements from your mapper will go to your reducer, and print statements
    from your reducer will be considered your final output.  By contrast, messages
    logged via the loggers we configured will be saved to two files, one
    for the mapper and one for the reducer.  If you hit "Test Run", then we
    will show the contents of those files once your program has finished running.
    The logging module also has other capabilities; see 
    https://docs.python.org/2/library/logging.html for more information.
    """

    pairs = []
    line_count = 0
    col_count = 0
    district = ""
    aadhar_gen = ""

    # DEBUG code: read from file instead of sys.stdin
    f = open('aadhaar_raw_data/aadhaar_data.csv', 'r')
    w = open('aadhaar_raw_data/mapreduce_intermed.txt', 'w')
    for line in f:

    #for line in sys.stdin:

        # get an array of the column values, the data is comma separated in the source file
        data = line.strip().split(",")
        
        # skip over the header row
        if line_count == 0:

            # get the number of columns in the header so that we can do a data integrity check on each row
            col_count = len(data)
            line_count+=1 
            continue
        
        if col_count == len(data):
            
            # get and clean the strings for district and aadhar_generated
            district = data[3]
            aadhar_gen = data[8]

            # put values in an array, which we will sort and then print to a file at the end for reducer consumption
            pairs.append(district + "\t" + aadhar_gen + "\n")
        else:
            # this means its a badly formed row and is missing values, skip it
            continue 

        line_count+=1

    # sort the pairs array
    pairs.sort()
    for value in pairs:

        # DEBUG code, write values to a file for reducer consumption
        w.write(value)

        # emit the pair
        print value

    # DEBUG code, close the files
    f.close()
    w.close()

def reducer():

    '''
    Given the output of the mapper for this exercise, the reducer should return
    one row per unit, along with the total number of ENTRIESn_hourly over the
    course of May (which is the duration of our data).

    You can assume that the input to the reducer is sorted by UNIT, such that all rows
    corresponding to a particular UNIT are grouped together.

    The output should have a unit (the key) follow by a tab, follow by a value.
    An example output row from the reducer might look like this:
    R001\t500625.0

    Since you are printing the actual output of your program, you
    can't print a debug statement without breaking the grader.
    Instead, you should use the logging module, which we've configured
    to log to a file which will be printed when you hit "Test Run".
    For example:
    logging.info("My debugging message")
    '''

    aadhaar_generated = 0
    old_key = None

    # DEBUG code, read from file instead of sys.stdin
    f = open('aadhaar_raw_data/mapreduce_intermed.txt', 'r')
    for line in f:

    #for line in sys.stdin:
    
        # get an array of the column values, the data is comma separated in the source file
        data = line.strip().split("\t")
        # error check the row
        if len(data) <>  2:
            # badley formed row, skip it
            continue

        curr_key, aadhaar_count = data

        # if we are seeing a new print the values for the total sum we tallied for the key we finished
        if old_key <> None and old_key <> curr_key:
            print old_key + "\t" + str(aadhaar_generated)
            aadhaar_generated = 0

        # assign the new key, add the value of aadhaar count to the running total
        old_key = curr_key
        aadhaar_generated+=float(aadhaar_count)

    if old_key <> None:
        print old_key + "\t" + str(aadhaar_generated)

    # DEBUG code, close the file
    f.close()

if __name__ == "__main__":

    mapper()
    reducer()
