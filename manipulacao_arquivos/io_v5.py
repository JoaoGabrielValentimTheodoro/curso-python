#!/usr/bin/python3

if __name__ == "__main__":
    # Streaming de arquivo
    with open("pessoas.csv") as arquivo:
        for registro in arquivo:
            print("Nome: {}, Idade: {}".format(*registro.strip().split(",")))

    if arquivo.closed:
        print("Arquivo finalizado.")
