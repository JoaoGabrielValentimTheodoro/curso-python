#!/usr/bin/python3
generator = (i ** 2 for i in range(11) if i % 2 == 0)

for numero in generator:
    print(f"Valor: {numero}")
