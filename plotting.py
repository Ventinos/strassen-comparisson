from typing import List, Tuple
import matplotlib.pyplot as plt
from formulas import *

X = []
default_time = []
strassen_time = []

default_calc = []
strassen_calc = []

# reading the values from the files:
with open('sizes.txt', 'r') as arquivo:
  for line in arquivo:
    X.append(float(line))

with open('default.txt', 'r') as arquivo:
  for line in arquivo:
    default_time.append(float(line))

with open('strassen.txt', 'r') as arquivo:
  for line in arquivo:
    strassen_time.append(float(line))


for i in X:
  strassen_calc.append(strassen_estimate(i))
  default_calc.append(pow(i,3))

figure, axis = plt.subplots(2, 2)

axis[0, 0].plot(X, strassen_time, marker='o', linestyle='-', color='b')
axis[0, 0].grid(True)
axis[0, 0].set_title("Tempo real de Strassen")


axis[0, 1].plot(X, default_time, marker='o', linestyle='-', color='r')
axis[0, 1].grid(True)
axis[0, 1].set_title("Tempo real da multiplicação simples")


axis[1, 0].plot(X, strassen_calc, marker='o', linestyle='-', color='b')
axis[1, 0].grid(True)
axis[1, 0].set_title("Tempo calculado de Strassen")


axis[1, 1].plot(X, default_calc, marker='o', linestyle='-', color='r')
axis[1, 1].grid(True)
axis[1, 1].set_title("Tempo calculado da multiplicação simples")

# Combine all the operations and display 
plt.show()

# New Plot, 2 functions in one plot, comparisson:
plt.plot(X, strassen_time, marker='o', linestyle='-', color='b',label='Strassen')
plt.plot(X, default_time, marker='o', linestyle='-', color='r', label='Iterativo simples')

plt.legend(loc='best')
# Combine all the operations and display 
plt.show()
