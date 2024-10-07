from multiprocessing.dummy import Value

import pytest
import matrix

def matrix_methods(method, argument):
    try:
        arg1 = argument[0]
        arg2 = argument[1]
        if isinstance(arg1, (int, float)):
            function = getattr(arg1, method)(matrix.Matrix(arg2))
        elif isinstance(arg2, (int, float)):
            function = getattr(matrix.Matrix(arg1), method)(arg2)
        else:
            function = getattr(matrix.Matrix(arg1), method)(matrix.Matrix(arg2))
        return function
    except:
        raise ValueError

@pytest.mark.parametrize("method, result, argument",
        [
        ("__add__",
        [[7, 8, 9], [1, 9, 5]],
        [[[5, 5, 5], [1, 8, 2]], [[2, 3, 4], [0, 1, 3]]]),
        ("__eq__", False,
        [[[5, 5, 5, 4], [1, 8, 2, 7]], [[2, 3, 4], [0, 1, 3]]]),
        ("__eq__", True,
        [[[3, 1 , 7], [3, 7, 9]], [[3, 1, 7], [3, 7, 9]]]),
        ("__mul__", [[6, 2, 14], [6, 14, 18]],
        [[[3, 1 , 7], [3, 7, 9]], 2]),
        ("__mul__", [[73, 68, 35], [137, 92, 43]],
        [[[3, 1 , 7], [3, 7, 9]], [[3, 8, 9], [8, 2, 1], [8, 6, 1]]]),
        ])
def test_methods_matrix(method, result, argument):
    tested_function = matrix_methods(method, argument)
    try:
        assert tested_function == result
    except:
        assert tested_function.raw_matrix == result

@pytest.mark.parametrize("raw_matrix, power, result",
    [([[5, 2], [4, 8]], 2, [[33, 26], [52, 72]]),
     ([[5, 2, 5], [4, 8, 7], [1, 9, 9]], 4,
     [[9833, 25303, 25577], [17157, 43959, 44432], [18495, 47570, 47946]])])
def test_square_matrix_pow(raw_matrix, power, result):
    test_result = matrix.SquareMatrix(raw_matrix) ** power
    assert test_result.raw_matrix == result

@pytest.mark.parametrize("raw_matrix, method, result",
                         [([[3, 4, 5], [2, 8.0, 7.1]],
                           "__str__",
"""3 4 5
2 8.0 7.1"""),
                        ([[0, 0, 0], [0, 0, 0]], '__str__',
"""0 0 0
0 0 0"""),
                          ])
def test_str_matrix(raw_matrix, method, result):
    assert str(matrix.Matrix(raw_matrix)) == result


@pytest.mark.parametrize("method, expected_exception, argument",
        [
        ("__add__",
        ValueError,
        [[[5, 5, 5, 4], [1, 8, 2, 4]], [[2, 3, 4], [0, 1, 3]]]),
        ("__add__",
        ValueError,
        [[[5, 5, 5], [1, 8, 2]], [[2, 3, 4], [0, 1, 3], [2, 2, 1]]]),
        ("__eq__", ValueError,
        [[[5, 5, "5", 4], [1, 8, 2, 3]], [[2, 3, 4], [0, 1, 3]]]),
        ("__eq__", ValueError,
        ["[[3, 1 , 7], [3, 7, 9]]", [[3, 1, 7], [3, 7, 9]]]),
        ("__mul__", ValueError,
        [3, 2]),
        ("__mul__", ValueError,
        [[[3, 1 , 7, 5], [3, 7, 9, 8]], [[3, 8, 9], [8, 2, 1], [8, 6, 1]]]),
        ("__mul__", ValueError,
        [[[3, 1 , 7], [3, 7, 9]], [[3, 8, 9], [8, 2, 1], [8, 6, 1], [1, 2, 1]]]),
        ])
def test_methods_matrix_broken(method, expected_exception, argument):
    with pytest.raises(expected_exception):
        tested_function = matrix_methods(method, argument)
        tested_function