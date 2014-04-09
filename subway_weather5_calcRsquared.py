import numpy
import pandas
import scipy
import matplotlib.pyplot as plt

def normalize_features(array):
   """
   Normalize the features in our data set.
   """
   array_normalized = (array-array.mean())/array.std()
   mu = array.mean()
   sigma = array.std()

   return array_normalized, mu, sigma

def compute_cost(features, values, theta):
    """
    Compute the cost function given a set of features / values, and the values for our thetas.
    
    This should be the same code as the compute_cost function in the lesson #3 exercises. But
    feel free to implement your own.
    """
    
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    
    This is the same gradient descent code as in the lesson #3 exercises. But feel free
    to implement your own.
    """
    m = len(values)
    cost_history = []

    for i in range(num_iterations):
        newcost = compute_cost(features, values, theta)
        cost_history.append(newcost)
        
        theta = theta + alpha * numpy.dot(values - numpy.dot(features,theta),features)
                  
    return theta, pandas.Series(cost_history)

def predictions(dataframe):
    '''
    The NYC turnstile data is stored in a pandas dataframe called weather_turnstile.
    Using the information stored in the dataframe, lets predict the ridership of
    the NYC subway using linear regression with gradient descent.
    
    You can look at information contained in the turnstile weather dataframe 
    at the link below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv    
    
    Your prediction should have a R^2 value of .40 or better.
    
    Note: due to the memory and CPU limitation of our amazon EC2 instance, we will
    give you a random subet (~15%) of the data contained in turnstile_data_master_with_weather.csv
    
    If you receive a "server has encountered an error" message, that means you are hitting 
    the 30 second  limit that's placed on running your program. Try using a smaller number
    for num_iterations if that's the case.
    
    Or if you are using your own algorithm/modesl, see if you can optimize your code so it
    runs faster.
    '''
    dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    #print dummy_units
    features = dataframe[['rain', 'precipi', 'Hour', 'meantempi']].join(dummy_units)
    values = dataframe[['ENTRIESn_hourly']]
    m = len(values)

    features, mu, sigma = normalize_features(features)

    features['ones'] = numpy.ones(m)
    features_array = numpy.array(features)
    values_array = numpy.array(values).flatten()

    #Set values for alpha, number of iterations.
    alpha = .00001 # please feel free to play with this value
    num_iterations = 20 # please feel free to play with this value

    #Initialize theta, perform gradient descent
    #print len(features.columns)
    theta_gradient_descent = numpy.zeros(len(features.columns))
    theta_gradient_descent, cost_history = gradient_descent(features_array, values_array, theta_gradient_descent,
                                                            alpha, num_iterations)

    predictions = numpy.dot(features_array, theta_gradient_descent)
    

    return predictions


def plot_residuals(turnstile_weather, predictions):
    '''
    Using the same methods that we used to plot a histogram of entries
    per hour for our data, why don't you make a histogram of the residuals
    (that is, the difference between the original hourly entry data and the predicted values).

    Based on this residual histogram, do you have any insight into how our model
    performed?  Reading a bit on this webpage might be useful:

    http://www.itl.nist.gov/div898/handbook/pri/section2/pri24.htm
    '''
    
    plt.figure()
    #print "mean of residuals (should be about 0): " + str((turnstile_weather['ENTRIESn_hourly'] - predictions).mean())
    (turnstile_weather['ENTRIESn_hourly'] - predictions).hist()
    plt.show()
    return plt

def compute_r_squared(data, predictions):
    '''
    In exercise 5, we calculated the R^2 value for you. But why don't you try and
    and calculate the R^2 value yourself.
    
    Given a list of original data points, and also a list of predicted data points,
    write a function that will compute and return the coefficient of determination (R^2)
    for this data.  numpy.mean() and numpy.sum() might both be useful here, but
    not necessary.

    Documentation about numpy.mean() and numpy.sum() below:
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html
    '''

    r_squared = 0
    
    theMeanEntries = numpy.mean(data)
    #print "the mean is: " + str(theMeanEntries) 

    # this is the actual values (the 'y's) minus the mean for all the dependent values (again, the 'y's) then squared
    denominator_df = numpy.square(data - theMeanEntries)
    
    # this is the actual values (the 'y's) minus the predicted values for 'y'...in other words, the residuals...then squared
    numerator_df = numpy.square(data - predictions)

    r_squared = 1 - (numerator_df.sum() / denominator_df.sum())
    
    #print "r squared = " + str(r_squared)
    
    return r_squared


if __name__ == "__main__":

    filename = "combined_weather_mta_raw_data/turnstile_data_master_with_weather.csv"
    weatherdata = pandas.read_csv(filename)
    thePredictions = predictions(weatherdata)
    #plot_residuals(weatherdata,thePredictions)
    
    data = weatherdata['ENTRIESn_hourly']
    compute_r_squared(data, thePredictions)
