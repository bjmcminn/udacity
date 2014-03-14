import pandas

def add_full_name(path_to_csv, path_to_new_csv):
    #Assume you will be reading in a csv file with the same columns that the
    #Lahman baseball data set has -- most importantly, there are columns
    #called 'nameFirst' and 'nameLast'.
    #1) Write a function that reads a csv
    #located at "path_to_csv" into a pandas dataframe, adds a new column
    #called 'nameFull' with a players full name.
    #
    #For example:
    #   for Hank Aaron, nameFull would be 'Hank Aaron', 
	#
	#2) Write the data in the pandas dataFrame to a new csv file located at
	#path_to_new_csv

    imported_data = pandas.read_csv(path_to_csv)
    # print imported_data
    # print imported_data["nameFirst"]
    imported_data["nameFull"] = imported_data["nameFirst"] + " " + imported_data["nameLast"]
    imported_data.to_csv(path_to_new_csv, index=0)

 

    #for theIndex, player in imported_data.iterrows():
        #debug code
        #1==0
        #print str(theIndex)

add_full_name("lahman_raw_data/Master.csv", "modified_Master.csv")
