import pytest
import input_handler
from input_handler import space_separated


@pytest.mark.parametrize("rows_num, columns_num, attribute, result",
[(3, 3,
        "func",
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
])
def test_space_separated_init(rows_num, columns_num, attribute, result):
    assert input_handler.IdentityMatrix(rows_num, columns_num).__dict__[attribute] == result

@pytest.mark.parametrize("rows_num, columns_num, attribute, expected_exception", [
        ("""3 5 1 4 2 1
8 7 2 2 4 5
4 3 2.1 3 4 5""", 3,
         "determinant",
         TypeError),
])
def test_initialization_broken(rows_num, columns_num, attribute, expected_exception):
    with pytest.raises(expected_exception):
        input_handler.IdentityMatrix(rows_num, columns_num).__dict__[attribute]
