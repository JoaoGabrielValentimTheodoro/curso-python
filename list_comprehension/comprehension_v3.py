#!/usr/bin/python3
if __name__ == "__main__":
    generator = (i ** 2 for i in range(11) if i % 2 == 0)
    print(f"{next(generator)}")
    print(f"{next(generator)}")
    print(f"{next(generator)}")
    print(f"{next(generator)}")
    print(f"{next(generator)}")
    print(f"{next(generator)}")
    # print(f"{next(generator)}") # Erro!
