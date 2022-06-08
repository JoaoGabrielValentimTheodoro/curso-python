#!/usr/bin/python3

if __name__ == "__main__":
    # Streaming de arquivo
    arquivo = open("pessoas.csv")
    for registro in arquivo:
        print("Nome: {}, Idade: {}".format(*registro.strip().split(",")))
    arquivo.close()
