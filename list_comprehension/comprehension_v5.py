#!/usr/bin/python3
if __name__ == "__main__":
    dicionario = {f"Item {i}": i * 2 for i in range(11) if i % 2 == 0}
    print(f"{dicionario}")

    for item, dobro in dicionario.items():
        print(f"{item} : {dobro}")
