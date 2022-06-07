#!/usr/bin/python3
# 0, 1, 1, 2, 3, 5,8, 13, 21...

def fibonnaci(quantidade, sequencia=(0, 1)):
    # implementar condição de parada
    return sequencia if len(sequencia) == quantidade else \
        fibonnaci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == "__main__":
    for fib in fibonnaci(20):
        print(fib)
