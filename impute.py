import pandas
import numpy

def imputation(filename):
    # Pandas dataframes have a method called 'fillna(value)', such that you can
    # pass in a single value to replace any NAs in a dataframe or series. You
    # can call it like this: 
    #     dataframe['column'] = dataframe['column'].fillna(value)
    #
    # Using the numpy.mean function, which calculates the mean of a numpy
    # array, impute any missing values in our Lahman baseball
    # data sets 'weight' column by setting them equal to the average weight.
    # 
    # You can access the 'weight' colum in the baseball data frame by
    # calling baseball['weight']

    df_baseball = pandas.read_csv(filename)

    theMean = 0
    theMean = numpy.mean(df_baseball["weight"])
    #print theMean
    df_baseball["weight"] = df_baseball["weight"].fillna(theMean)

    return df_baseball

if __name__ == "__main__":
    imputation("lahman_raw_data/Master.csv")
