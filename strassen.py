from matrix import *
from typing import List, Tuple


def actual_strassen(matrix_a: List, matrix_b: List) -> List:
  """
  Recursive function to calculate the product of two matrices, using the Strassen Algorithm.  It only supports even length matrices.
  """
  if matrix_dimensions(matrix_a) == (2, 2):
    return matrix_multiplication(matrix_a, matrix_b)

  a, b, c, d = split_matrix(matrix_a)
  e, f, g, h = split_matrix(matrix_b)

  t1 = actual_strassen(a, matrix_subtraction(f, h))
  t2 = actual_strassen(matrix_addition(a, b), h)
  t3 = actual_strassen(matrix_addition(c, d), e)
  t4 = actual_strassen(d, matrix_subtraction(g, e))
  t5 = actual_strassen(matrix_addition(a, d), matrix_addition(e, h))
  t6 = actual_strassen(matrix_subtraction(b, d), matrix_addition(g, h))
  t7 = actual_strassen(matrix_subtraction(a, c), matrix_addition(e, f))

  top_left = matrix_addition(matrix_subtraction(matrix_addition(t5, t4), t2),t6)
  top_right = matrix_addition(t1, t2)
  bot_left = matrix_addition(t3, t4)
  bot_right = matrix_subtraction(matrix_subtraction(matrix_addition(t1, t5), t3), t7)

  # construct the new matrix from our 4 quadrants
  top_combined = np.concatenate((top_left, top_right), axis=1)
  bot_combined = np.concatenate((bot_left, bot_right), axis=1)
  new_matrix = np.concatenate((top_combined, bot_combined), axis=0)

  return new_matrix
