import input_handler

input_command = int(input("Enter the type of matrix equation (1 or 2):\n 1 - Ax=B\n 2 - xA=B\n"))
row_a = int(input("Input number of rows for matrix A: "))
a = input_handler.SquareMatrix(input_handler.space_separated_row_by_row(row_a))
row_b = int(input("Input number of rows for matrix B: "))
b = input_handler.SquareMatrix(input_handler.space_separated_row_by_row(row_b))

if input_command == 1:
    res = a.inverse_matrix * b
    print(res)
elif input_command == 2:
    res = b * a.inverse_matrix
    print(res)
else:
    print('Input is not correct')
