import sys
import math
import random
from time import time
from typing import List, Tuple
import matplotlib.pyplot as plt

from matrix import *
from strassen import *
"""Argv content description:
  * Argv[0] = rows
  * Argv[1] = columns
  * Argv[2] = min_number in matrix
  * Argv[3] = max_number in matrix
"""


def main():
  rows = int(sys.argv[1])
  columns = int(sys.argv[2])
  min_number = int(sys.argv[3])
  max_number = int(sys.argv[4])
  matrix1 = [[random.randrange(min_number, max_number) for _ in range(rows)]
             for _ in range(columns)]

  matrix2 = [[random.randrange(min_number, max_number) for _ in range(rows)]
             for _ in range(columns)]

  # getting default time:
  t0 = time()
  # default matrix multiplication
  multiply_default(matrix1, matrix2)
  t1 = time()
  default_time = t1 - t0

  # getting strassen time:
  t0 = time()
  # strassen matrix multiplication
  actual_strassen(matrix1, matrix2)
  t1 = time()
  strassen_time = t1 - t0

  # saving time at files:
  with open('default.txt', 'a') as arquivo:
    arquivo.write(str(default_time) + '\n')

  with open('strassen.txt', 'a') as arquivo:
    arquivo.write(str(strassen_time) + '\n')

  # saving n:
  with open('sizes.txt', 'a') as arquivo:
    arquivo.write(str(rows) + '\n')


if __name__ == "__main__":
  main()
