import pytest
import operations
from input_handler import space_separated
from matrix import raw_matrix_type


@pytest.mark.parametrize("method, result, args",
        [("multiply_scalar",
        [[15, 20, 25], [10, 40.0, 35.5]],
        [[[3, 4, 5], [2, 8.0, 7.1]], 5]),
        ("multiply_scalar",
        [[0, 0, 0], [0, 0, 0]],
        [[[3, 4, 5], [2, 8.0, 7.1]], 0]),
        ("multiply_matrix",
        [[54], [78]],
        [[[2, 6], [2, 9]], [[3], [8]]]),
        ("__add__",
        [[7, 8, 9], [1, 9, 5]],
        [[[5, 5, 5], [1, 8, 2]], [[2, 3, 4], [0, 1, 3]]]),
        ("__eq__", True,
        [[[5, 5, 5], [1, 8, 2]], [[2, 3, 4], [0, 1, 3]]]),
        ("__eq__", True,
        [[[3, 1 , 7], [3, 7, 9]], [[3, 1, 7], [3, 7, 9]]]),
        ("__mul__", [[6, 2, 14], [6, 14, 18]],
        [[[3, 1 , 7], [3, 7, 9]], 2]),
        ("__mul__", [[6, 2, 14], [6, 14, 18]],
        [[[3, 1 , 7], [3, 7, 9]], [[3, 8, 9], [8, 2, 1], [8, 6, 1]]]),
        ])
def test_operate_matrix(method, result, args):
    raw_matrix = args[0]
    operand = args[1]
    tested_function = getattr(operations, method)
    try:
        assert tested_function(operations.Matrix(raw_matrix), operand)
    except:
        assert tested_function(operations.Matrix(raw_matrix), operations.Matrix(operand))

@pytest.mark.parametrize("matrix, power, result",
    [([[5, 2]], 2, [[25, 4]])])
def test_square_matrix_pow(matrix, power, result):
    assert operations.Matrix(matrix) ** power == result


def test_square_matrix_inverse()

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
        [([[3, "4", 5], [2, 8.0, 7.1]],
        "transpose",
        TypeError),
        ("[[3, 2, 1]]", "transpose", TypeError),
         (" ", 'transpose', TypeError),
        ])
def test_init_broken(raw_matrix, method, expected_exception):
    with pytest.raises(expected_exception):
        getattr(input_handler.Matrix(raw_matrix), method).__dict__["raw_matrix"]