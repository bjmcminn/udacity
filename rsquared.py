import numpy

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    data_mean = numpy.mean(data)
    numerator = numpy.square(numpy.subtract(data,predictions)).sum()
    denominator = numpy.square(numpy.subtract(data, data_mean)).sum()
    r_squared = 1 - (numerator / denominator)
    
    return r_squared
