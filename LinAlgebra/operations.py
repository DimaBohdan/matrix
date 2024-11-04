from typing import Dict, List

from LinAlgebra.matrix import Matrix
import re
import numpy as np

operators = set('()+-*^T')


class ShuntingYard:
    def __init__(self):
        self.operators = {
            '+': {'precedence': 1, 'associativity': 'L'},
            '-': {'precedence': 1, 'associativity': 'L'},
            '*': {'precedence': 2, 'associativity': 'L'},
            '^': {'precedence': 3, 'associativity': 'R'},
            'T': {'precedence': 4, 'associativity': 'R'},
        }

    def is_operator(self, token: str) -> bool:
        return token in self.operators

    def precedence(self, operator: str) -> int:
        return self.operators[operator]['precedence']

    def associativity(self, operator: str) -> str:
        return self.operators[operator]['associativity']

    def to_postfix(self, tokens: list) -> list:
        output_queue = []
        operator_stack = []  # type: list[list]

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


def evaluate_postfix(tokens: list) -> Matrix | int | float:
    stack = []
    for token in tokens:
        if isinstance(token, (Matrix, int, float)):
            stack.append(token)
        elif token in operators:
            if token == "T":
                a = stack.pop()
                stack.append(a.transpose())
            else:
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

    return stack[0]


def tokenize(expression: str, matrices_dict: dict) -> list:
    tokens = []
    temp = ''

    def add_temp_token(temp: str | int | float):
        if re.match(r'^\d*\.?\d+$', temp):
            tokens.append(float(temp) if '.' in temp else int(temp))
        elif temp:  # Check if temp is not empty
            try:
                tokens.append(matrices_dict[temp])
            except KeyError:
                raise ValueError(
                    f"Unknown variable or matrix '{temp}' in expression.")

    for char in expression:
        if char in operators:
            add_temp_token(temp)
            temp = ''  # Reset temp
            tokens.append(char)
        elif char.isalnum() or char == '.':
            temp += char
        elif char.isspace():
            add_temp_token(temp)
            temp = ''
    add_temp_token(temp)
    return tokens

def evaluate_expression(expression: str,
                        matrix_dict: Dict[str,
                                          List[List[str | int | float]]]):
    try:
        matrix_vars = {name: Matrix(np.array(value))
                       for name, value in matrix_dict.items()}
        sy = ShuntingYard
        expression_handler = ShuntingYard()
        tokens = tokenize(expression, matrix_vars)
        postfix = sy.to_postfix(expression_handler, tokens)
        actual_result = evaluate_postfix(postfix)
        return actual_result.raw_matrix.tolist()
    except Exception as e:
        raise ValueError(f"Error in evaluating expression: {e}")
