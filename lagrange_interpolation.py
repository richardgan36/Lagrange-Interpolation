import numpy as np
import math
import matplotlib.pyplot as plt

from time_test import time_test

"""Plots the lagrange polynomial for a set of points"""


# Interpolates a set of points using the Lagrange polynomial, implemented using NumPy
@time_test
def lagrange_interpolation_numpy(points: list, num_points_to_plot: int):
    # Points is a 2-d Python list of shape (N, 2)
    points = np.array(points)
    idx_sorted_by_x = np.argsort(points[:, 0])
    points = points[idx_sorted_by_x]  # sort in ascending order of x
    x, y = points[:, 0], points[:, 1]
    N = x.size
    x_to_plot = np.linspace(x[0], x[-1], num_points_to_plot)

    # Formula for Lagrange polynomial
    # p(x) = sum(Li * fi), i = 0, 1, 2, ..., N
    # Li = prod( (xp-xm) / (xi-xm) ), 0 <= m <= N, m != i

    # Evaluate p(x)
    xp = np.repeat(x_to_plot, N*(N-1)).reshape((num_points_to_plot, N, -1))

    xm = np.repeat(np.expand_dims(x, axis=0), repeats=N, axis=0)
    xm_mask = ~np.identity(N).astype(bool)  # false along the main diagonal
    xm = xm[xm_mask].reshape(N, -1)
    xm = np.repeat(np.expand_dims(xm, axis=0), num_points_to_plot, axis=0)

    xi = np.repeat(x, repeats=N-1).reshape((N, -1))
    xi = np.repeat(np.expand_dims(xi, axis=0), num_points_to_plot, axis=0)

    L = np.prod((xp-xm)/(xi-xm), axis=2)
    px = np.sum(L * y, axis=1)

    return x_to_plot, px


# Interpolates a set of points using the Lagrange polynomial, implemented using for loops
@time_test
def lagrange_interpolation_for_loop(points: list, num_points_to_plot: int):
    # Points is a 2-d Python list of shape (N, 2)
    points = sorted(points)  # sort in ascending order of x
    x, y = [point[0] for point in points], [point[1] for point in points]
    N = len(x)
    step = (x[-1] - x[0]) / (num_points_to_plot - 1)
    x_to_plot = [x[0] + i * step for i in range(num_points_to_plot)]
    y_to_plot = []

    # Formula for Lagrange polynomial
    # p(x) = sum(Li * fi), i = 0, 1, 2, ..., N
    # Li = prod( (xp-xm) / (xi-xm) ), 0 <= m <= N, m != i

    # Evaluate p(x)
    for xp in x_to_plot:
        p_xp = 0  # initialise p(xp)
        for i in range(N):  # p(xp) += Li * fi
            Li = 1  # initialise Li
            for j in range(N):  # calculate Li
                if j == i:
                    continue

                Li *= (xp-x[j]) / (x[i] - x[j])

            p_xp += Li * y[i]

        y_to_plot.append(p_xp)

    return x_to_plot, y_to_plot


def plot_lagrange_interpolation(x_to_plot: list, y_to_plot: list, x: list, y: list):
    plt.plot(x_to_plot, y_to_plot)
    plt.scatter(x, y)
    plt.title("Lagrange Interpolation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
