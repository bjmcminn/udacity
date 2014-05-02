import logging
import sys
import string
import re

# Commented for debugging
#from util import logfile

#logging.basicConfig(filename=logfile, format='%(message)s',
                   #level=logging.INFO, filemode='w')


def mapper():

    #Your mapper code goes here.
    #You will also need to fill out the reducer
    #code as well before test running or else you will get an error.

    #Each line will be
    #a comma-separated list of values.  The
    #header row WILL be included.  Tokenize
    #each row using the commas, and emit a key-
    #value pair containing the district and
    #Aadhaar generated, separated by a tab.
    #Make sure each row has the correct number
    #of tokens and is not the header row!

    #You can see a copy of the the input aadhaar data
    #in the link below:
    #https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv

    #Since you are printing the actual output of your program, you
    #can't print a debug statement without breaking the grader.
    #Instead, you should use the logging module, which we've configured
    #to log to a file which will be printed when you hit "Test Run".
    #For example:
    #logging.info("My debugging message")

    #your code here

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

    #Cycle through the list of key-value pairs emitted
    #by your mapper, and print out each key once,
    #along with the total number of Aadhaar generated,
    #separated by a tab.  Assume that the list of key-
    #value pairs will be ordered by key.  Make sure
    #each key-value pair is formatted correctly!
    #Here's a sample final key-value pair: "Gujarat\t5.0"

    #Since you are printing the actual output of your program, you
    #can't print a debug statement without breaking the grader.
    #Instead, you should use the logging module, which we've configured
    #to log to a file which will be printed when you hit "Test Run".
    #For example:
    #logging.info("My debugging message")

    # your code here

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
