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
