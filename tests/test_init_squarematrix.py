import pytest
import input_handler
from input_handler import space_separated


@pytest.mark.parametrize("raw_matrix, method, result",
        [([[3, 4, 5], [2, 8.0, 7.1], [1, 1, 1]],
        "transpose",
        [[3.0, 2.0, 1], [4.0, 8.0, 1], [5, 7.1, 1]]),
        ([[3, 2, 1, 0], [3, 2, 1, 0], [3, 2, 1, 0], [3, 2, 1, 0]], "transpose",
        [[3, 3, 3, 3], [2, 2, 2, 2], [1, 1, 1, 1], [0, 0, 0, 0]]),
        ([[0, 2.3], [0, 2.1]], 'transpose', [[0, 0], [2.3, 2.1]]),
        ([[3, 4, 5], [2, 8.0, 7.1], [1, 1, 1]], "cofactor",
        [[0.9, 5.1, -6], [1, -2, 1], [-11.6, -11.3, 16]]),
        ([[1]], "cofactor", [[1]])
          ])
def test_init_property(raw_matrix, method, result):
    function = getattr(input_handler.SquareMatrix(raw_matrix), method).__dict__["raw_matrix"]
    assert function == result


@pytest.mark.parametrize("raw_matrix, method, result",
                         [([[3, 4, 5], [2, 8.0, 7.1], [1, 1, 1]],
                           "determinant",
                           -6.9),
                          ([[3]], "determinant", 3),
                          ([[2, 3], [1, 8]], "determinant", 13)
                          ])
def test_init_property_digit(raw_matrix, method, result):
    function = getattr(input_handler.SquareMatrix(raw_matrix), method)
    assert function == result


@pytest.mark.parametrize("raw_matrix, method, result",
                         [([[3, 4, 5], [2, 8.0, 7.1]],
                           "__str__",
"""3 4 5
2 8.0 7.1"""),
                        ([[0, 0, 0], [0, 0, 0]], '__str__',
"""0 0 0
0 0 0"""),
                          ])
def test_init_str(raw_matrix, method, result):
    assert str(input_handler.Matrix(raw_matrix)) == result


@pytest.mark.parametrize("raw_matrix, method, expected_exception",
        [([[3, "4", 5], [2, 8.0, 7.1], [1, 2, 3]],
        "transpose",
        TypeError),
        ("[[3, 2, 1], [2, 3, 4], [4.6, 8,9, 1,1]]", "transpose", TypeError),
         (" ", 'transpose', TypeError),
        ([[2, 2, 3]], "determinant", TypeError),
        ([[0.9, 5.1, -6], [1, -2, 1]], "cofactor", TypeError)
        ])
def test_init_broken(raw_matrix, method, expected_exception):
    with pytest.raises(expected_exception):
        getattr(input_handler.SquareMatrix(raw_matrix), method).__dict__["raw_matrix"]