#!/usr/bin/python3

if __name__ == "__main__":
    arquivo = open("pessoas.csv")
    dados = arquivo.read()
    arquivo.close()
    for registro in dados.splitlines():
        print("Nome: {} , Idade: {}".format(*registro.split(",")))
