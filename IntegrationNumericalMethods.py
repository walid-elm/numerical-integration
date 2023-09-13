#!/usr/bin/env python
# coding: utf-8

"""

@author: walidelmouahidi

"""

# %% Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% Integral Universal Function


class Integral:
    """
    Integral is a versatile class for approximating the area under a given function f(x) over a specified interval [a, b].

    It provides four different numerical integration methods:

    1. Trapezoid Method
    2. Midpoint Method
    3. Simpson's Method
    4. Monte Carlo Method

    Usage:
        integral = Integral(f, a, b, n)
        result = integral.trapezoidal()   # Calculate integral using the Trapezoid method
        result = integral.midpoint()      # Calculate integral using the Midpoint method
        result = integral.simpson()       # Calculate integral using Simpson's method
        result = integral.montecarlo(N)   # Calculate integral using the Monte Carlo method

    Args:
        f (function): The function to be integrated.
        a (float): The lower bound of the integration interval.
        b (float): The upper bound of the integration interval.
        n (int): The number of intervals used for approximation.

    Methods:
        - trapezoidal(): Approximates the integral using the Trapezoid method.
        - midpoint(): Approximates the integral using the Midpoint method.
        - simpson(): Approximates the integral using Simpson's method.
        - montecarlo(N): Approximates the integral using the Monte Carlo method with N random samples.
    """

    def __init__(self, f, a, b, n):
        """
        Initializes the Integral object with the function, integration bounds, and number of intervals.

        Args:
            f (function): The function to be integrated.
            a (float): The lower bound of the integration interval.
            b (float): The upper bound of the integration interval.
            n (int): The number of intervals used for approximation.
        """
        self.h = abs(b - a) / n
        self.a = a
        self.b = b
        self.n = n
        self.f = f
        self.xs = np.arange(self.a, self.b + self.h, self.h)

    def trapezoidal(self):
        """
        Approximates the integral using the Trapezoid method.

        Returns:
            float: The estimated value of the integral.
        """
        res = 0
        for i in range(self.n):
            res = res + (self.f(self.xs[i + 1]) +
                         self.f(self.xs[i])) * (self.h / 2)
        return res

    def midpoint(self):
        """
        Approximates the integral using the Midpoint method.

        Returns:
            float: The estimated value of the integral.
        """
        res = 0
        for i in range(self.n):
            res = res + self.h * self.f(self.a + self.h / 2 + i * self.h)
        return res

    def simpson(self):
        """
        Approximates the integral using Simpson's method.

        Returns:
            float: The estimated value of the integral.
        """
        res = 0
        for i in range(1, self.n + 1):
            res = res + self.h / 6 * (self.f(self.a + i * self.h - self.h) +
                                      4 * self.f(self.a + i * self.h - self.h / 2) +
                                      self.f(self.a + i * self.h))
        return res

    def montecarlo(self, N):
        """
        Approximates the integral using the Monte Carlo method.

        Args:
            N (int): The number of random samples to use for estimation.

        Returns:
            float: The estimated value of the integral.
        """
        self.ys = self.f(self.xs)
        up = max(self.ys)
        low = min(self.ys)
        self.p1 = 0
        self.tot_area = abs(up - low) * abs(self.b - self.a)

        for i in range(N):
            x = np.random.uniform(self.a, self.b)
            y = np.random.uniform(low, up)
            if y <= self.f(x):
                self.p1 = self.p1 + 1

        self.p1 = self.p1 / N
        res = self.p1 * self.tot_area
        return res

# %% Example


def g(x):
    return x**2


g_Integral = Integral(g, 0, 2, 1000)

act = 8/3  # actual integral value, found analitically
a1 = g_Integral.trapezoidal()
a2 = g_Integral.midpoint()
a3 = g_Integral.simpson()
a4 = g_Integral.montecarlo(10000)

results = pd.DataFrame()
results["Metrics"] = ["result", "error"]
results["Trapezoid"] = [a1, abs(act-a1)]
results["Mid Point"] = [a2, abs(act-a2)]
results["Simpson"] = [a3, abs(act-a3)]
results["Mone Carlo"] = [a4, abs(act-a4)]
results = results.set_index("Metrics")

results
