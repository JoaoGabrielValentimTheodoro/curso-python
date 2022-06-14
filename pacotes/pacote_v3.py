#!/usr/bin/python3
from pacote1 import modulo1
from pacote2 import modulo1 as sub

if __name__ == "__main__":
    print(sub.subtracao(10, 20))
    print(modulo1.soma(1, 2, 3, 4))
