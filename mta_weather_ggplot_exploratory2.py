from pandas import *
from ggplot import *
import pandasql
import time

def plot_weather_data(turnstile_weather):

    ''' 
    You are given a pandas dataframe called turnstile_weather. 
    Use it along with ggplot to make another data visualization focused on the MTA and weather
    data we used in assignment #3. 
    
    You should make a type of visualization that is different than what you did in exercise #1.
    Try to use the data in a different way (e.g., if you made a lineplot concerning ridership 
    and time of day in exercise #1, maybe look at weather and try to make a histogram in exercise #2). 
    Or attempt to use multiple encodings in your graph if you haven't in the previous exercise.
    
    You should feel free to implement something that we discussed in class
    (e.g., scatterplots, line plots, or histograms) or attempt to implement 
    something more advanced if you'd like.  Here are some suggestions for things
    to investigate and illustrate:
    * Ridership by time of day or day of week
    * How ridership varies based on Subway station
    * Which stations have more exits or entries at different times of day

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
    
    You can check out: 
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
    
    However, due to the limitation of our Amazon EC2 server, we are giving you about 1/5
    of the actual data in the turnstile_weather dataframe
    '''

    #debug code that does the groupby using panadas function rather than SQL, this works too
    #NOTE: for the udacity submission, could not use pandasql and so submission uses this groupby function rather than sql
    #meanentries=[]
    #meanentries = turnstile_weather.groupby('UNIT',as_index=False).mean()

    #grouped_by_unit = turnstile_weather.groupby('UNIT',as_index=False)

    #grouped_by_unit['avgentries'] = meanentries

    # Query to group the entries volume data by Date



    print turnstile_weather.columns
    turnstile_weather = turnstile_weather.drop('Unnamed: 0',1)
    print turnstile_weather

    q = """
    SELECT
        UNIT,
        rain,
        AVG(ENTRIESn_hourly) avgentries
    FROM 
        turnstile_weather w
    GROUP BY
        UNIT, rain
    HAVING
        avgentries>4000
        AND rain in (0,1)
    ORDER BY
        rain, avgentries desc
    """

    #Execute SQL command against the pandas frame
    grouped_by_unit = pandasql.sqldf(q, locals())

    #Create a new index to order the data by
    index_array=[]
    iterval = 0
    for z in grouped_by_unit['UNIT']:
        index_array.append(iterval)
        iterval+=1
    
    grouped_by_unit['newindex']=index_array

    #Print for debugging purposes
    print grouped_by_unit 
    
    #Plot the resulting dataframe: show a bar graph that depicts volume for highest volume turnstiles in rain vs. non rain conditions
    plot = ggplot(grouped_by_unit, aes(x='newindex', weight='avgentries', color='rain')) \
        + geom_bar() \
        + ggtitle('NY MTA Entries for Top Volume Turnstiles \n in Rain vs. No Rain ') + xlab('No Rain (L) and Rain (R)') + ylab('Avg Turnstile Entries')
    
    
    return plot
    

if __name__ == "__main__":

    filename = "combined_weather_mta_raw_data/turnstile_data_master_with_weather.csv"
    # This would be how ideally I create the dataframe to avoid having to delete the unnamed index column
    #thedata = pandas.read_csv(filename, index_col=0)

    thedata = pandas.read_csv(filename)
    print plot_weather_data(thedata)
