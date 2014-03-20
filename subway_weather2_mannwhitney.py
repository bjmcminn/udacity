import numpy as np
import scipy
import scipy.stats
import pandas

def mann_whitney_plus_means(turnstile_weather):
    '''
    This function will consume the turnstile_weather dataframe containing
    our final turnstile weather data. 
    
    You will want to take the means and run the Mann Whitney U test on the 
    ENTRIESn_hourly column in the turnstile_weather dataframe.
    
    This function should return:
        1) the mean of entries with rain
        2) the mean of entries without rain
        3) the Mann-Whitney U statistic and p-value comparing number of entries
           with rain and the number of entries without rain.  
    
    You should feel free to use scipy's Mann-Whitney implementation, and
    also might find it useful to use numpy's mean function.  
    
    Here are some documentations:
    http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    
    You can look at the final turnstile weather data at the link below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''
    with_rain_mean = 0
    without_rain_mean = 0
    U = 0
    p = 0

    norain = turnstile_weather[turnstile_weather['rain']==0]
    without_rain_mean = norain['ENTRIESn_hourly'].mean()

    yesrain = turnstile_weather[turnstile_weather['rain']==1]
    with_rain_mean = yesrain['ENTRIESn_hourly'].mean()

    U,p = scipy.stats.mannwhitneyu(norain['ENTRIESn_hourly'], yesrain['ENTRIESn_hourly'])

    print with_rain_mean
    print without_rain_mean
    print U
    print p
    

    #print turnstile_weather.ix[1:50,1:12]
    
    return with_rain_mean, without_rain_mean, U, p


if __name__ == "__main__":

    filename = "combined_weather_mta_raw_data/turnstile_data_master_with_weather.csv"
    weatherdata = pandas.read_csv(filename)
    mann_whitney_plus_means(weatherdata)
