#!/usr/bin/python3.5
"""

The Module composed by a function that multiplies 2 matrices

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """A function that multiplies 2 matrices

    Args:
        m_a: The matrix a
        m_b: The matrix b

    Returns:
        The result of the multiplication


    """

    return (np.matmul(m_a, m_b))
