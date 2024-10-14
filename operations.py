from matrix import Matrix
import numpy as np

operators = set('()+-*^~')
class ShuntingYard:
    def __init__(self):
        self.operators = {
            '+': {'precedence': 1, 'associativity': 'L'},
            '-': {'precedence': 1, 'associativity': 'L'},
            '*': {'precedence': 2, 'associativity': 'L'},
            '^': {'precedence': 3, 'associativity': 'R'},
            '~': {'precedence': 4, 'associativity': 'R'}
        }

    def is_operator(self, token: str) -> bool:
        return token in self.operators

    def precedence(self, operator: str) -> int:
        return self.operators[operator]['precedence']

    def associativity(self, operator: str) -> str:
        return self.operators[operator]['associativity']

    def to_postfix(self: "ShuntingYard", tokens: list) -> list:
        output_queue = []
        operator_stack = []

        for token in tokens:
            if isinstance(token, (Matrix, int, float)):
                output_queue.append(token)
            elif self.is_operator(token):
                while (operator_stack and operator_stack[-1] != '(' and
                       (self.precedence(operator_stack[-1]) > self.precedence(token) or
                        (self.precedence(operator_stack[-1]) == self.precedence(token) and
                         self.associativity(token) == 'L'))):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                operator_stack.pop()  # Pop the '('

        while operator_stack:
            output_queue.append(operator_stack.pop())

        return output_queue

    @staticmethod
    def evaluate_postfix(tokens: list) -> Matrix:
        stack = []
        for token in tokens:
            if isinstance(token, (Matrix, int, float)):
                stack.append(token)
            elif token in operators:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "^":
                    stack.append(a ** b)
                elif token == "~":
                    stack.append(~b)
        return stack[0]


def tokenize(expression: str, matrices_dict: dict) -> list:
    tokens = []
    temp = ''

    def add_temp_token(temp: str):
        if temp.isdigit():
            tokens.append(int(temp))
        elif temp:  # Check if temp is not empty
            try:
                tokens.append(matrices_dict[temp])
            except KeyError:
                raise ValueError(f"Unknown variable or matrix '{temp}' in expression.")

  # Use a set for efficient lookup
    for char in expression:
        if char in operators:
            add_temp_token(temp)
            temp = ''  # Reset temp
            tokens.append(char)
        elif char.isalnum():
            temp += char
        elif char.isspace():
            add_temp_token(temp)
            temp = ''
    add_temp_token(temp)
    return tokens


# Example usage
A = Matrix(np.array([[1, 2], [3, 4]]))
B = Matrix(np.array([[2, 0], [1, 3]]))
matrices_dict = {'A': A, 'B': B}

expression = ("(A * 2)^3^(-1)")
tokens = tokenize(expression, matrices_dict)
print("Tokens:", tokens)

shunting_yard = ShuntingYard()
postfix = shunting_yard.to_postfix(tokens)
print("Postfix:", postfix)

result = shunting_yard.evaluate_postfix(postfix)
print("Result:\n", result)