import pytest
import numpy as np
from sympy.logic.algorithms.lra_theory import LRARational

from LinAlgebra.matrix import Matrix


A = Matrix(np.array([[5, 4, 5], [4, 2, 1]]))
B = Matrix(np.array([[2, 7.8, 34], [6.8, 5.9, 23]]))
C = Matrix(np.array([[5, 4], [4, 2], [5, 1]]))
D = Matrix(np.array([[7, 11.8, 39], [10.8, 7.9, 24]]))
E = Matrix(np.array([[5, 4, 0], [4, 2, -2], [5, 1, 0]]))
F = Matrix(np.array([[8.1, 4, 0], [4, 5.1, -2], [5, 1, 3.1]]))
G = Matrix(np.array([[-4, -4, 0], [-4, -1, 2], [-5, -1, 1]]))
H = Matrix(np.array([[-36, -24, 8], [-14, -16, 2], [-24, -21, 2]]))
J = Matrix(np.array([[18, 12, -4], [7, 8, -1], [12, 10.5, -1]]))
K = Matrix(np.array([[1, 2, 2], [1, -1, 0], [0, -2, 0]]))
L = Matrix(np.array([[0, 1, -0.5], [0, 0, -0.5], [0.5, -0.5, 0.75]]))
M = Matrix(np.array([[-0.25, 0.25, -0.875], [-0.25, 0.25, -0.375], [0.375, 0.125, 0.5625]]))
N = Matrix(np.array([[32, 20, -8], [10, 15, 0], [19, 20, -1]]))

def test_matrix_transpose():
    assert A.transpose() == C
def test_add_matrices():
    assert A + B == D
def test_add_num():
    assert 3.1 + E == F
def test_sub_matrices():
    assert 1 - E == G
def test_sub_num():
    assert 1-E == G
def test_mul_matrices():
    assert E * G == H
def test_mul_num():
    assert (E * G) * -0.5 == J
def test_inverse():
    assert ~K == L
def test_plus_power():
    assert G ** 2 == N
def test_negative_power():
    assert K ** -2 == M
def test_zero_power():
    assert J ** 0 == Matrix(np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))