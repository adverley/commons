# Connectivity matrices
# Used in DTW, clustering, reservoir computing ...
import numpy as np


def connect_with_prev_and_next_only(N: int, connect_with_self: bool = False):
    '''
    :return: np array with ones on the sub and superdiagonal:
    0   1   0   0
    1   0   1   0
    0   1   0   1
    0   0   1   0
    '''
    mtrx = np.zeros((N, N), dtype=float)
    np.fill_diagonal(mtrx[1:, :], 1)
    np.fill_diagonal(mtrx[:, 1:], 1)
    if connect_with_self:
        np.fill_diagonal(mtrx, 1)

    return mtrx


if __name__ == '__main__':
    # test
    m = connect_with_prev_and_next_only(5, connect_with_self=True)
    print(m)