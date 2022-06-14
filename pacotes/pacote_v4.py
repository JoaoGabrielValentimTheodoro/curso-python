#!/usr/bin/python3
from pacote1.modulo1 import soma
from pacote2.modulo1 import subtracao as sub

if __name__ == "__main__":
    print("Soma", soma(1, 3))
    print("Subtração", sub(2, 22))
