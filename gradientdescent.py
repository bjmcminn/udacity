import numpy
import pandas

def compute_cost(features, values, theta):
    """
    Compute the cost function given a set of features / values, and values for our thetas.
    """
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent():
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    # Write some code here that updates the values of theta a number of times equal to
    # num_iterations.  Everytime you have computed the cost for a given set of thetas,
    # you should append it to cost_history.  The function should return both the final
    # values of theta and the cost history.
    cost_history = []
    print features
    for x in xrange(num_iterations):
        newcost = compute_cost(features, values, theta)
        cost_history.append(newcost)
        
        theta = theta + alpha * numpy.dot(values - numpy.dot(features,theta),features)
                
                                                     
    return theta, pandas.Series(cost_history)

if __name__ == "__main__":

    filename = "baseball_data_raw/baseball_data.csv"
    gradient_descent()
