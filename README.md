# Numerical Integration Software

This software provides a flexible framework for numerically calculating definite integrals using different methods. You can easily approximate the area under a given function over a specified interval using one of the following methods:

1. Trapezoid Method
2. Midpoint Method
3. Simpson's Method
4. Monte Carlo Method

## Introduction

Numerical integration is a fundamental technique in mathematics and computer science that allows us to approximate the definite integral of a function over a specified interval. It has applications in various fields, including physics, engineering, and data analysis.

## Trapezoid Method

The Trapezoid Method approximates the integral by dividing the area under the curve into trapezoids and summing their areas. It provides a reasonably accurate estimate for smooth functions.

## Midpoint Method

The Midpoint Method approximates the integral by evaluating the function at the midpoint of each subinterval and summing the areas of rectangles. It can be more accurate than the Trapezoid Method for certain functions.

## Simpson's Method

Simpson's Method uses quadratic interpolation to approximate the integral. It divides the interval into subintervals and fits a parabolic curve to each subinterval. This method can provide very accurate results for well-behaved functions.

## Monte Carlo Method

The Monte Carlo Method estimates the integral by generating random samples within the integration bounds and computing the fraction of points that fall under the curve. While it's a stochastic method, it can be particularly useful for complex or irregular functions.

## Example

Let's calculate the integral of the function $f(x) = x^{2}$ over the interval $[0, 2]$ using each of the four methods with $1000$ intervals:

| Method       | Result       | Error          |
|--------------|--------------|----------------|
| Trapezoid    | 2.666668     | 0.000001       |
| Midpoint     | 2.666666e+00 | 6.666667e-07   |
| Simpson      | 2.666667e+00 | 8.881784e-16   |
| Monte Carlo  | 2.639200     | 0.027467       |

In this example, you can see that each method provides an estimate of the integral along with an error metric. The choice of method depends on the function and desired accuracy.

Feel free to use this software to perform numerical integration for your own functions and applications.

