import pandas
import pandasql
import sys
import csv

def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt

    http://web.mta.info/developers/turnstile.html
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. 
    
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file in the links below:
    
    Sample input file:
    https://www.dropbox.com/s/mpin5zv4hgrx244/turnstile_110528.txt
    Sample updated file:
    https://www.dropbox.com/s/074xbgio4c39b7h/solution_turnstile_110528.txt
    '''
    for name in filenames:
        f = open(name, 'rb') 
        w = open("updated_" + name, "wb")
        reader = csv.reader(f)
        writer = csv.writer(w)
        rowcounter = 0
        for row in reader:
            rowcounter+=1
            #Each row has 3 id columns, then some number of sets of 5 columns with turnstile data.  
            num_sets = (len(row)-3)/ 5
            num_cols_per_set = 5
            sets_counter = 0
            cols_counter = 0

            #3 id columns

            while sets_counter < num_sets:
                newrow = []
                newrow.append(row[0])
                newrow.append(row[1])
                newrow.append(row[2])
                while cols_counter < num_cols_per_set:
                    #print "index for row " + str(rowcounter) + " is: "  + str((sets_counter*num_cols_per_set)+cols_counter+3) + " and value  is " + str(row[(sets_counter*num_cols_per_set)+cols_counter+3])
                    newrow.append(row[(sets_counter*num_cols_per_set)+cols_counter+3])
                    cols_counter+=1
                
                cols_counter=0
                sets_counter+=1
                
                #print newrow
                writer.writerow(newrow)
                
        w.close()        
        f.close()



if __name__ == "__main__":

    filelist = []
    filelist.append("turnstile_110514.txt")
    filelist.append("turnstile_110507.txt")
    fix_turnstile_data(filelist)
