@staticmethod
def same_dimension(func: Callable[[Matrix, Matrix], Any]) -> Callable[[Matrix, Matrix], Any]:
    @wraps(func)
    def wrapper(this: Matrix, other: Matrix) -> Any:
        if this.matrix_shape == other.matrix_shape:
            return func(this, other)
        else:
            raise ValueError("Matrices should have same dimensions to do this action!")

    return wrapper


@staticmethod
def is_multipliable(func: Callable[[Matrix, Matrix], Any]) -> Callable[[Matrix, Matrix], Any]:
    @wraps(func)
    def wrapper(this: Matrix, other: Matrix) -> Any:
        if this.matrix_shape[1] == other.matrix_shape[0]:
            return func(this, other)
        else:
            raise ValueError("Unable to do this action, invalid matrices!")

    return wrapper


@staticmethod
def __only_squared(func: Callable[[Matrix, Any], Any]) -> Callable[[Matrix, Any], Any]:
    @wraps(func)
    def wrapper(matrix: Matrix, *args: Any, **kwargs: Any) -> Any:
        if matrix.is_square:
            return func(matrix, *args, **kwargs)
        else:
            raise ValueError("Matrix should be squared to do this action!")

    return wrapper


@staticmethod
def __only_vector(func: Callable[[Matrix, Any], Any]) -> Callable[[Matrix, Any], Any]:
    @wraps(func)
    def wrapper(self, *args, **kwargs) -> Any:
        if self.is_row_vector() or self.is_column_vector():
            return func(self, *args, **kwargs)
        else:
            raise ValueError("Matrix should be vector to do this action!")

    return wrapper


@staticmethod
def __only_invertible(func: Callable[[Matrix, Any], Any]) -> Callable[[Matrix, Any], Any]:
    @wraps(func)
    def wrapper(self, *args, **kwargs) -> Any:
        if self.determinant() != 0:
            return func(self, *args, **kwargs)
        else:
            raise ValueError("Matrix should be invertible to do this action!")

    return wrapper


@staticmethod
def __only_able_to_power(func: Callable[[Matrix, int], Any]) -> Callable[[Matrix, int], Any]:
    @wraps(func)
    def wrapper(self, power, *args, **kwargs) -> Any:
        if power % 1 == 0:
            return func(self, power, *args, **kwargs)
        else:
            raise ValueError("Power should be a whole number to do this action!")

    return wrapper
