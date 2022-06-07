#!/usr/bin/python3
# 0, 1, 1, 2, 3, 5,8, 13, 21...

def fibonnaci():
    penultimo = 0
    ultimo = 1
    print(f"{penultimo}, {ultimo}", end=", ")
    while True:
        proximo = penultimo + ultimo
        print(f"{proximo}", end=", ")
        penultimo = ultimo
        ultimo = proximo


if __name__ == "__main__":
    fibonnaci()
