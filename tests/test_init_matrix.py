import pytest
import numpy as np
from LinAlgebra.matrix import Matrix


A = Matrix(np.array([[5, 4, 5], [4, 2, 1]]))
B = Matrix(np.array([[2, 7.8, 34], [6.8, 5.9, 23]]))
C = Matrix(np.array([[5, 4], [4, 2], [5, 1]]))
D = Matrix(np.array([[7, 11.8, 39], [10.8, 7.9, 24]]))
E = Matrix(np.array([[5, 4, 0], [4, 2, -2], [5, 1, 0]]))
F = Matrix(np.array([[8.1, 4, 0], [4, 5.1, -2], [5, 1, 3.1]]))
G = Matrix(np.array([[-4, -4, 0], [-4, -1, 2], [-5, -1, 1]]))


def test_matrix_transpose():
    assert A.transpose() == C
def test_add_matrices():
    assert A+B == D
def test_add_num():
    assert 3.1+E == F
def test_sub_num():
    assert 1-E == G