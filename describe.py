import pandas
import sys

def getDescribe(path):
    f = open('describe_OUT.txt', 'w')
    df_theData = pandas.read_csv(path)
    
    f.write("---SUMMARY OF COLUMNS---\n\n" + str(df_theData) + "\n\n\n")
    
    df_description = df_theData.describe()
    
    f.write("---SUMMARY STATISTICS BY COLUMN---\n\n")
    
    for stat_index, theStat in df_description.iterkv():
        f.write(str(stat_index) + "\n" +  str(theStat) + "\n")
    
    f.close()
    
if __name__ == "__main__":
    
    path = sys.argv[1]
    getDescribe(path)

