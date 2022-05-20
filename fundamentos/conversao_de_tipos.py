2 + 3
# print(2 + "3")
a = 2
b = "3"

print(type(a))  # <class 'int'>
print(type(b))  # <class 'str'>
print(a + int(b))  # str to int
print(str(a) + b)  # int to str

# print(2 + int("2 legal")) # operação inválida
# print(2 + int("3.4")) # operação inválida

print(2 + float("3.4"))  # str to float
