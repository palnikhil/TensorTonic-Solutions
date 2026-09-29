import numpy as np

def finite_difference_derivative(coefficients: list, x: float, h: float) -> tuple[float, float, float]:
    """
    Returns the value at x, the value at x plus h, and the estimated slope.
    """
    def polynomial_func(input: float):
        max_power = len(coefficients)
        complete_fx=0.0
        for i in range(0,max_power):
            complete_fx += coefficients[i]*(input ** i)

        return complete_fx

    value_at_x = polynomial_func(x)
    value_at_x_h = polynomial_func(x+h)

    estimated_slope = (value_at_x_h - value_at_x)/h

    return value_at_x,value_at_x_h, estimated_slope
