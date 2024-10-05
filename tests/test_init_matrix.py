import pytest
import input_handler
from input_handler import space_separated


@pytest.mark.parametrize("raw_matrix, method, result",
        [([[3, 4, 5], [2, 8.0, 7.1]],
        "transpose",
        [[3.0, 2.0], [4.0, 8.0], [5, 7.1]]),
        ([[3, 2, 1]], "transpose", [[3], [2], [1]]),
         ([[0, 0, 0], [0, 0, 0]], 'transpose', [[0, 0], [0, 0], [0, 0]]),
        ])
def test_init_property(raw_matrix, method, result):
    function = getattr(input_handler.Matrix(raw_matrix), method).__dict__["raw_matrix"]
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
        [([[3, "4", 5], [2, 8.0, 7.1]],
        "transpose",
        TypeError),
        ("[[3, 2, 1]]", "transpose", TypeError),
         (" ", 'transpose', TypeError),
        ])
def test_init_broken(raw_matrix, method, expected_exception):
    with pytest.raises(expected_exception):
        getattr(input_handler.Matrix(raw_matrix), method).__dict__["raw_matrix"]