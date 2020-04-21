import numpy as np


def sample_log(min_value, max_value, n):
    """
    Samples logarithmically between min_value and max_value.
    :param min_value: minimum value of log random sampling
    :param max_value: maximum value of log random sampling
    :param n: how many samples do you want?
    :return: n logarithmaically sampled numbers between min and max as a numpy array.

    Example:
    min_learning_rate = 0.0001
    max_learning_rate = 1

    will explore the region [0.0001, 0.001] as much as [0.1, 1]
    """
    a = np.log10(min_value)
    b = np.log10(max_value)

    log_r = np.random.random(size=n)  # between [0, 1)
    log_r = (b - a) * log_r + a  # scale up

    r = np.power(10, log_r)

    return r
