""" [summary]

Returns
-------
[type]
    [description]
"""
import numpy as np


def pagerank(M, num_iterations=100, d=0.85):
    """pagerank: Trillion dollar algorithm.

    Parameters
    ----------
    M : numpy array
        adjacency matrix where M_i,j represents the link from 'j' to 'i',
        such that for all 'j' sum(i, M_i,j) = 1]
    num_iterations : int, optional
        number of iterations, by default 100
    d : float, optional
        damping factor, by default 0.85

    Returns
    -------
    numpy array
        a vector of ranks such that v_i is the i-th rank from [0, 1],
        v sums to 1

    """
    N = M.shape[1]
    v = np.random.rand(N, 1)
    v = v / np.linalg.norm(v, 1)
    iteration = 0
    while iteration < num_iterations:
        iteration += 1
        v = d * np.matmul(M, v) + (1 - d) / N
    return v
