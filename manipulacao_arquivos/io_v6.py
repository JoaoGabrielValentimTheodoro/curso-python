#!/usr/bin/python3

if __name__ == "__main__":
    # Streaming de arquivo
    with open("pessoas.csv") as arquivo:
        with open("pessoas.txt", "w") as saida:
            for registro in arquivo:
                pessoas = registro.strip().split(",")
                print("Nome: {}, Idade: {}".format(*pessoas), file=saida)

    if arquivo.closed:
        print("Arquivo de entrada finalizado.")

    if saida.closed:
        print("Arquivo de saida finalizado.")
