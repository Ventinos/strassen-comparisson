#!/bin/bash

# Loop sobre as potências de 2 de 2 a 1048576
for ((x = 2; x <= 2048; x *= 2)); do
    # Chamada para main.py com os valores de x, x, 0 e 100 como argumentos
    python3 main.py $x $x 0 100
done

