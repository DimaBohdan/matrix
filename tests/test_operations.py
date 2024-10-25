import numpy as np
import pytest
import csv

from LinAlgebra.matrix import Matrix
from LinAlgebra.operations import ShuntingYard as sy
A = Matrix(np.array([[3, 5, 2, 12],
                     [12, 3, 45, 3],
                     [1, 3, -3, 8],
                     [-4, 6, 30, 9]]))
B = Matrix(np.genfromtxt("tests/test_csv_files/next_random_7x5.csv",
                    delimiter=",", dtype=float))
C = Matrix(np.genfromtxt("tests/test_csv_files/random_5x7.csv",
                    delimiter=",", dtype=float))
D = Matrix(np.genfromtxt("tests/test_csv_files/random_7x5.csv",
                    delimiter=",", dtype=float))
E = Matrix(np.genfromtxt("tests/test_csv_files/random_4x4",
                    delimiter=",", dtype=float))
G = Matrix(np.genfromtxt("tests/test_csv_files/squared_uninvertable_10x10.csv",
                    delimiter=",", dtype=float))
F = Matrix(np.array([[3, 15, 6],
                    [3, 5, 6],
                    [12, 9, 8]]))
H = Matrix(np.array([[4, 5, 13],
                    [6, 8, 9],
                    [20, 3, 8]]))
J = Matrix(np.genfromtxt("tests/test_csv_files/squared_invertible_10x10.csv",
                    delimiter=",", dtype=float))
matrix_dict = {
    "A":A,
    "B":B,
    "C":C,
    "D":D,
    "E":E,
    "F":F,
    "G":G,
    "H":H,
    "J":J,
}
@pytest.mark.parametrize("expression, result",
                         [
                          ("F-H", 516),
                          ("F+H", 1064),
                          ("F * H", -498240),
                          ("F * (H+4)", -676800),
                          ("(F-5)^2*H - 20*(H+13)", -698290230),
                          ])
def test_expression_find_determinant(expression, result):
    expession_handler = sy()
    tokens = sy.tokenize(expression, matrix_dict)
    postfix = sy.to_postfix(expession_handler, tokens)
    actual_result = sy.evaluate_postfix(postfix)
    assert float(actual_result.determinant()) == result