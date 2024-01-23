# Functions and Recursion
# Author: Ricco C
# 7 December 2023

import time

def factorial(n: int) -> int:
    """Return the nth factorial.
    Done recursively.

    Example:
        factorial(3) -> 3! -> 6
    """
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return factorial(n - 1) * n


def fib(n: int) -> int:
    """Return the nth Fibonacci number.
    Calculated recursively.
    """
    if n in [1, 2]:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)

def fib_itr(n: int) -> int:
    """Returns the nth Fibinacci number.
    Calculated iterativley
    """
    last_num = 0
    num = 1
    result = 1

    for i in range(n - 1):
        result = num + last_num

        num, last_num = result, num

    return result

# print(factorial(100))
print(fib(5), fib_itr(5))

time_initial = time.perf_counter()
fib(20)
time_final = time.perf_counter()

print(f"Recurive: {time_final-time_initial}")

time_initial = time.perf_counter()
fib_itr(20)
time_final = time.perf_counter()
print(f"Iterative: {time_final-time_initial}")