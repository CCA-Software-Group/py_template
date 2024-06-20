import numpy as np 

from py_template.example_module import fibonacci

def test_fibonacci():
    """Check the Fibonacci sequence function"""
    fib = fibonacci(10)
    np.testing.assert_allclose(actual=fib, 
                               desired=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55],
                               rtol=1e0,
    )