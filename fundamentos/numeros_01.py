# print(dir(int), dir(float))
# int & float
a = 5
b = 2.5
print(a / b)
print(a + b)
print(a * b)

print(type(a), type(b))
print(b.is_integer(), 5.0.is_integer())  # Verify if is integer or float
# Internal Functions by int
print(int.__add__(2, 3))
print(2 + 3)
print((-2).__abs__())
print((-3.6).__abs__())
# Functions int
print(abs(-2))
print(abs(-3.6))
