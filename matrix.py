from typing import List, Tuple
def default_matrix_multiplication(a: List, b: List) -> List:
    """
    Multiplication only for 2x2 matrices
    """
    new_matrix = [
        [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],
    ]
    return new_matrix


def matrix_addition(matrix_a: List, matrix_b: List):
    return [
        [matrix_a[row][col] + matrix_b[row][col] for col in range(len(matrix_a[row]))]
        for row in range(len(matrix_a))
    ]


def matrix_subtraction(matrix_a: List, matrix_b: List):
    return [
        [matrix_a[row][col] - matrix_b[row][col] for col in range(len(matrix_a[row]))]
        for row in range(len(matrix_a))
    ]


def split_matrix(a: List,) -> Tuple[List, List, List, List]:
    """
    Given an even length matrix, returns the top_left, top_right, bot_left, bot_right quadrant.
    """
    matrix_length = len(a)
    mid = matrix_length // 2

    top_right = [[a[i][j] for j in range(mid, matrix_length)] for i in range(mid)]
    bot_right = [
        [a[i][j] for j in range(mid, matrix_length)] for i in range(mid, matrix_length)
    ]

    top_left = [[a[i][j] for j in range(mid)] for i in range(mid)]
    bot_left = [[a[i][j] for j in range(mid)] for i in range(mid, matrix_length)]

    return top_left, top_right, bot_left, bot_right


def matrix_dimensions(matrix: List) -> Tuple[int, int]:
    return len(matrix), len(matrix[0])


def print_matrix(matrix: List) -> None:
    for row in matrix:
        print(row)

def multiply_default(matrix_a,matrix_b):
  # Initialize the result matrix with zeros
  result = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]

  # Perform matrix multiplication
  for i in range(len(matrix_a)):
      for j in range(len(matrix_b[0])):
          for k in range(len(matrix_b)):
              result[i][j] += matrix_a[i][k] * matrix_b[k][j]

  return result
