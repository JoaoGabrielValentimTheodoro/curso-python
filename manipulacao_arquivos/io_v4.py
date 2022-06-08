#!/usr/bin/python3

if __name__ == "__main__":
    # Streaming de arquivo
    try:
        arquivo = open("pessoas.csv")
        for registro in arquivo:
            print("Nome: {}, Idade: {}".format(*registro.strip().split(",")))
    except IndexError:
        pass
    finally:
        print("Ok!")
        arquivo.close()

    if arquivo.closed:
        print("Arquivo finalizado.")
