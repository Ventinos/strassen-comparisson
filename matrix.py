import numpy as np

def matrix_multiplication(a, b):
    return np.dot(a,b)

def matrix_addition(matrix_a, matrix_b):
    return np.add(matrix_a, matrix_b)

def matrix_subtraction(matrix_a, matrix_b):
    return np.subtract(matrix_a, matrix_b)

def split_matrix(a):
    """
    Given an even length matrix, returns the top_left, top_right, bot_left, bot_rightquadrant.
    """
    matrix_length = len(a)
    mid = matrix_length // 2

    top_left = a[:mid, :mid]
    top_right = a[:mid, mid:]
    bot_left = a[mid:, :mid]
    bot_right = a[mid:, mid:]

    return top_left, top_right, bot_left, bot_right


def matrix_dimensions(matrix):
    return len(matrix), len(matrix[0])


def print_matrix(matrix):
    for row in matrix:
        print(row)

def default_matrix_multiplication(matrix_a, matrix_b):
  # Initialize the result matrix with zeros
  result = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]

  # Perform matrix multiplication
  for i in range(len(matrix_a)):
      for j in range(len(matrix_b[0])):
          for k in range(len(matrix_b)):
              result[i][j] += matrix_a[i][k] * matrix_b[k][j]

  return result
