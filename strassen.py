from matrix import *
from typing import List, Tuple


def actual_strassen(matrix_a: List, matrix_b: List) -> List:
  """
  Recursive function to calculate the product of two matrices, using the Strassen Algorithm.  It only supports even length matrices.
  """
  if matrix_dimensions(matrix_a) == (2, 2):
    return default_matrix_multiplication(matrix_a, matrix_b)

  a, b, c, d = split_matrix(matrix_a)
  e, f, g, h = split_matrix(matrix_b)

  t1 = actual_strassen(a, matrix_subtraction(f, h))
  t2 = actual_strassen(matrix_addition(a, b), h)
  t3 = actual_strassen(matrix_addition(c, d), e)
  t4 = actual_strassen(d, matrix_subtraction(g, e))
  t5 = actual_strassen(matrix_addition(a, d), matrix_addition(e, h))
  t6 = actual_strassen(matrix_subtraction(b, d), matrix_addition(g, h))
  t7 = actual_strassen(matrix_subtraction(a, c), matrix_addition(e, f))

  top_left = matrix_addition(matrix_subtraction(matrix_addition(t5, t4), t2),
                             t6)
  top_right = matrix_addition(t1, t2)
  bot_left = matrix_addition(t3, t4)
  bot_right = matrix_subtraction(
      matrix_subtraction(matrix_addition(t1, t5), t3), t7)

  # construct the new matrix from our 4 quadrants
  new_matrix = []
  for i in range(len(top_right)):
    new_matrix.append(top_left[i] + top_right[i])
  for i in range(len(bot_right)):
    new_matrix.append(bot_left[i] + bot_right[i])
  return new_matrix


def strassen(matrix1: List, matrix2: List) -> List:
  if matrix_dimensions(matrix1)[1] != matrix_dimensions(matrix2)[0]:
    raise Exception(
        f"Unable to multiply these matrices, please check the dimensions. \n"
        f"Matrix A:{matrix1} \nMatrix B:{matrix2}")
  dimension1 = matrix_dimensions(matrix1)
  dimension2 = matrix_dimensions(matrix2)

  if dimension1[0] == dimension1[1] and dimension2[0] == dimension2[1]:
    return matrix1, matrix2

  maximum = max(max(dimension1), max(dimension2))
  maxim = int(math.pow(2, math.ceil(math.log2(maximum))))
  new_matrix1 = matrix1
  new_matrix2 = matrix2

  # Adding zeros to the matrices so that the arrays dimensions are the same and also
  # power of 2
  for i in range(0, maxim):
    if i < dimension1[0]:
      for j in range(dimension1[1], maxim):
        new_matrix1[i].append(0)
    else:
      new_matrix1.append([0] * maxim)
    if i < dimension2[0]:
      for j in range(dimension2[1], maxim):
        new_matrix2[i].append(0)
    else:
      new_matrix2.append([0] * maxim)

  final_matrix = actual_strassen(new_matrix1, new_matrix2)

  # Removing the additional zeros
  for i in range(0, maxim):
    if i < dimension1[0]:
      for j in range(dimension2[1], maxim):
        final_matrix[i].pop()
    else:
      final_matrix.pop()
  return final_matrix
