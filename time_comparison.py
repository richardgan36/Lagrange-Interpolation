import math
import numpy as np
from lagrange_interpolation import lagrange_interpolation_numpy, lagrange_interpolation_for_loop

sigmoid = [[-1.5, 0.183],
           [-0.5, 0.378],
           [0, 0.5],
           [3, 0.953]]

sine = [[-math.pi, 0],
        [0, 0],
        [math.pi/2, 1],
        [-math.pi/2, -1],
        [math.pi, 0]]

a = np.expand_dims(np.arange(5), 1)
rand = np.random.normal(size=(5, 1))
random_func = np.hstack((a, rand)).tolist()

N_test = 5000

time_numpy_total, time_for_loop_total = 0, 0
for _ in range(N_test):
    t_numpy, _ = lagrange_interpolation_numpy(random_func, 1000)
    t_for_loop, _ = lagrange_interpolation_for_loop(random_func, 1000)

    time_numpy_total += t_numpy
    time_for_loop_total += t_for_loop

time_numpy_avg = time_numpy_total / N_test
time_for_loop_avg = time_for_loop_total / N_test

runtime_reduction = 100 * ((time_for_loop_avg - time_numpy_avg) / time_for_loop_avg)
performance_increase = 100 * ((time_for_loop_avg - time_numpy_avg) / time_numpy_avg)
print(f"Reduction in runtime: {runtime_reduction: .2f}%")
print(f"Increase in performance: {performance_increase: .2f}%")
print(f"The NumPy implementation is {time_for_loop_avg / time_numpy_avg: .2f} times faster")
