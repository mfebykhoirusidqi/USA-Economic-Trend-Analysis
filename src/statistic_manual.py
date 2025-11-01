import numpy as np

def mean(data):
    return np.sum(data) / len(data)

def geometric_mean(data):
    return np.prod(data) ** (1 / len(data))

def variance(data):
    m = mean(data)
    return np.sum((data - m)**2) / len(data)

def correlation(x, y):
    xm, ym = mean(x), mean(y)
    return np.sum((x - xm)*(y - ym)) / np.sqrt(np.sum((x - xm)**2) * np.sum((y - ym)**2))

def linear_regression(x, y):
    x_mean, y_mean = mean(x), mean(y)
    b1 = np.sum((x - x_mean)*(y - y_mean)) / np.sum((x - x_mean)**2)
    b0 = y_mean - b1 * x_mean
    return b0, b1
