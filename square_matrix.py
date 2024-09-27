from matrix import *
class SquareMatrix(Matrix):
    def minor(self, row, column):
        if self.rows_number == 1 and self.columns_number == 1:
            minor = self.determinant()
        else:
            minor = self.sub_matrix(row, column).determinant()
        return minor

    def adjunct(self, row, column):
        adjunct = (-1) ** (row + column) * self.minor(row, column)
        return adjunct

    def determinant(self):
        if self.rows_number == 1:
            return self.raw_matrix[0][0]

        if self.rows_number == 2:
            return self.raw_matrix[0][0] * self.raw_matrix[1][1] - self.raw_matrix[0][1] * self.raw_matrix[1][0]

        determinant = 0
        for row in self.range_rows_number:
            determinant += self.adjunct(row, 0) * self.raw_matrix[row][0]
        return determinant


    def cofactor(self):
        if self.rows_number != self.columns_number:
            return "Cannot find a cofactor for a non-square matrix"
        cofactor_matrix = []
        for row in self.range_rows_number:
            cofactor_row = [self.adjunct(row, column) for column in self.range_columns_number]
            cofactor_matrix.append(cofactor_row)
        return SquareMatrix(cofactor_matrix)

    def inverse_matrix(self):
        determinant = self.determinant()
        if determinant == 0:
            return "Cannot be inversed, because determinant equals to zero"
        transposed_cofactor_matrix = self.cofactor().transpose()
        inverse = transposed_cofactor_matrix * (1 / determinant)
        return inverse

    def __pow__(self, n):
        if n <= 0:
            return "Cannot raise a non-square matrix to a power"
        # Initialize the result as the identity matrix
        power = IdentityMatrix(self.rows_number, self.rows_number)
        while n > 0:
            if n % 2 == 1:
                power = power * self.origin
            self.origin *= self.origin
            n //= 2
        return power
