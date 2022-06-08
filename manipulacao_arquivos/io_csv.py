#!/usr/bin/python3
import csv

if __name__ == "__main__":
    # Streaming de arquivo
    with open("pessoas.csv") as entrada:
        for pessoa in csv.reader(entrada):
            print("Nome: {}, Idade: {}".format(*pessoa))
