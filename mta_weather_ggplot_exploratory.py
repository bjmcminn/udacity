from pandas import *
from ggplot import *
import pandasql
import time

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
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
     
    However, due to the limitation of our Amazon EC2 server, we are giving you about 1/3
    of the actual data in the turnstile_weather dataframe
    '''

    #debug code that does the groupby using panadas function rather than SQL, this works too
    #NOTE: for the udacity submission, could not use pandasql and so submission uses this groupby function rather than sql
    #testdf = turnstile_weather.groupby('DATEn',as_index=False).sum()
    #print testdf

    # Query to group the entries volume data by Date
    q = """
    SELECT
        DATEn,
        SUM(ENTRIESn_hourly) sumentries
    FROM 
        turnstile_weather w
    GROUP BY
        DATEn
    """

    #Execute SQL command against the pandas frame
    grouped_by_day = pandasql.sqldf(q, locals())

    #Convert the DATEn column to a datetime value (otherwise, it seems ggplot treats it as a string and can't plot it)
    grouped_by_day.DATEn = pandas.to_datetime(grouped_by_day.DATEn)

    #Sort the data by the DATEn column for plotting purposes
    grouped_by_day = grouped_by_day.sort('DATEn')

    #Get the day of week string values for each date in DATEn
    theDayNames = []
    theDateDOW = []
    for the_date_time in grouped_by_day['DATEn']:
        theDayNames.append(datetime.strftime(the_date_time,'%a'))
        theDateDOW.append(datetime.strftime(the_date_time, '%m-%d-%y') + "-" + datetime.strftime(the_date_time, '%a'))
    grouped_by_day['DayName'] = theDayNames
    grouped_by_day['DateDOW'] = theDateDOW

    #Convert the datetimes to just dates in the DATEn column.  I'm nor sure why, but if they are DateTimes, ggplot tries to rescale the horizontal
    #axis and it does so somewhat arbitrarily
    grouped_by_day.DATEn = [d.date() for d in grouped_by_day.DATEn]

    #Print for debugging purposes
    print grouped_by_day

    #Plot the resulting dataframe: show a line graph that shows ridership by date
    #plot = ggplot(grouped_by_day, aes('DATEn','sumentries')) + geom_point(color = 'red') + geom_line(color='red') + ggtitle('NY MTA Ridership Data') + xlab('Date') + ylab('Turnstile Entries')
    
    #Plot the resulting dataframe: show a bar graph that shows ridership by date
    plot = ggplot(grouped_by_day, aes(x='DATEn',y='sumentries')) \
        + geom_bar(aes(weight = 'sumentries'), fill='blue') \
        + ggtitle('NY MTA Ridership Data') + xlab('Date') + ylab('Turnstile Entries') \
        #+ theme(axis_text_x = element_text(angle = 90, vjust = 0.5, hjust=1))
    

    return plot

if __name__ == "__main__":

    filename = "combined_weather_mta_raw_data/turnstile_data_master_with_weather_TEST.csv"
    thedata = pandas.read_csv(filename)
    print plot_weather_data(thedata)
