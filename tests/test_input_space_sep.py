import pytest
import input_handler
from input_handler import space_separated


@pytest.mark.parametrize("raw_matrix, attribute, result",
[("""3 5 1
8 7 2
4 3 2""",
        "raw_matrix",
        [[3.0, 5.0, 1.0], [8.0, 7.0, 2.0], [4.0, 3.0, 2.0]]),
("""3 5
8 7
4 3""",
        "rows_number",
        3),
("""3 5 1 4 2 1
8 7 2 2 4 5
4 3 2.1 3 4 5""",
    "columns_number",
    6),
])
def test_space_separated_init(raw_matrix, attribute, result):
    assert input_handler.Matrix(space_separated(raw_matrix)).__dict__[attribute] == result

@pytest.mark.parametrize("raw_matrix, attribute, expected_exception", [
        ("""3 5 1 4 2 1
8 7 2 2 4 5
4 3 2.1 3 4 5""",
         "determinant",
         KeyError),
        ("""3 5 1 4 2 1
8 . 2 2 4 5
4 3 2.1 3 4 5""",
         "rows_number",
         ValueError),
    ("""2 3 1.5
2 3 1.4 3 4 1.1""",
     "is_square",
     ValueError),
        ([3, 5, 1, 4, 2, 1,
8, 7, 2, 2, 4, 5,
4, 3, 2.1, 3, 4, 5], "columns_number", ValueError),

])
def test_initialization_broken(raw_matrix, attribute, expected_exception):
    with pytest.raises(expected_exception):
        input_handler.Matrix(space_separated(raw_matrix)).__dict__[attribute]
