#!/home/joaogvt/.pyenv/versions/3.10.4/bin/python
for x in range(1, 11):
    if x % 2 == 0:
        continue  # Interrompe a iteração e vai pra proxima
    print(x)

for x in range(1, 11):
    if x == 5:
        break  # Sai do laço for
    print(x)

print("Fim")
