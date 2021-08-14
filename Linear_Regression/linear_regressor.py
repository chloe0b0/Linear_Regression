import numpy as np
import matplotlib.pyplot as plt

class linear_regression:
    def __init__(self):
        self.alpha, self.beta = None, None

    def __str__(self):
        return f"y = {self.alpha} + {self.beta}*x"

    def fit(self, X, y):
        ''' input: two numpy arrays of equivalent shape
            output: the alpha, beta parameters for the best fit line '''
        if np.shape(X) != np.shape(y):
            raise ValueError("Matrix Shapes are not equivalent")

        X_mean, y_mean = np.mean(X), np.mean(y)

        numerator = np.sum((X - X_mean) * (y - y_mean))
        denominator = np.sum((X - X_mean) ** 2)
        self.beta = numerator / denominator
        self.alpha = y_mean - self.beta * X_mean    
    
    def pred(self, X):
        if not self.alpha or not self.beta:
            raise ValueError("alpha and or beta is None")
        return self.alpha + self.beta*X