import timeit
import math


def time_test(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        # print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        # return result
        return end_time - start_time, result
    return wrapper
