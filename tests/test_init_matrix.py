import pytest
from matrix import Matrix

@pytest.mark.parametrize("raw_matrix, attribute, result", [
    ([[2, 1, 7], [4, 1, 9], [4, 5, 6]], "raw_matrix", [[2, 1, 7], [4, 1, 9], [4, 5, 6]])
])
def test_initialization(raw_matrix, attribute, result):
    assert Matrix(raw_matrix).__dict__[attribute] == result
    
