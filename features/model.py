"""Module to contain all functions for building and teststing a logistic
regression model"""

import numpy as np

def sigmoid(X, theta):
    '''
    Returns the sigmoid of  theta.T.X
    Precondition: if X is (m x n), theta should be (n x i)
    '''
    return 1/(1+np.exp(-np.dot(X,theta)))

def computeCost(X, theta, y):
    '''
    Returns the cost for a particular choice of theta.
    '''
    m = X.shape[0]
    h = sigmoid(X, theta)
    cost = (1/m)*np.sum(-y*np.log(h)-(1-y)*np.log(1-h))
    return cost

def gradientDescent(X, theta, y, alpha=0.1, iters=1000, track=False):
    '''
    Optimises theta via gradient descent. If track==True, the cost is computed
    50 times at intervals to track convergence.
    '''
    m = X.shape[0]
    costs = []
    for i in range(iters+1):
        h = sigmoid(X, theta)
        gradients = (1/m)*np.dot(X.T,(h-y))
        theta = theta - alpha*gradients
        # Compute costs
        if track and ((i) % (iters/50) == 0):
            costs.append(computeCost(X, theta, y))
    if track:
        return theta, costs
    return theta

def predict(X, theta, threshold=0.5):
    '''Returns absolute predictions for all entries in X'''
    predictions = sigmoid(X, theta)
    return (predictions >= threshold).astype(int)

def predictAccuracy(predictions, y, pcnt=True):
    '''Returns prediction accuracy as percentage if pcnt==True, otherwise
    returns proportion.
    Precondition: len(predictions) ==  len(y)'''
    if pcnt:
        return "{:.2f}%".format(100*float((predictions == y).mean()))
    else:
        return (predictions == y).mean()

def precision(predictions, y):
    '''
    Calculate model precision.
    '''
    true_pos = ((predictions == 1) & (y == 1)).sum()
    false_pos = ((predictions == 1) & (y == 0)).sum()

    return true_pos/(true_pos+false_pos)

def recall(predictions, y):
    '''
    Calculate model precision.
    '''
    true_pos = ((predictions == 1) & (y == 1)).sum()
    false_neg = ((predictions == 0) & (y == 1)).sum()

    return true_pos/(true_pos+false_neg)

def f1score(predictions, y):
    '''
    Calculates F1 score as a prediction metric
    '''
    p = precision(predictions, y)
    r = recall(predictions, y)

    return (2*p*r)/(p + r)
