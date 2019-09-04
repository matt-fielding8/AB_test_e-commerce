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
