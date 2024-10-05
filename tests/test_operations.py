import pytest
import operations
from input_handler import space_separated
from matrix import raw_matrix_type


@pytest.mark.parametrize("method, result, args",
        [("multiply_scalar",
        [[15, 20, 25], [10, 40.0, 35.5]],
        [[[3, 4, 5], [2, 8.0, 7.1]], 5]),
        ()
        ])
def test_init_property(method, result, args):
    raw_matrix = args[0]
    operand = args[1]
    tested_function = getattr(operations, method)
    assert tested_function(operations.Matrix(raw_matrix), operand)

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