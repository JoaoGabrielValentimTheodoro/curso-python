a = {1, 2, 3, 4}  # conjunto
# a[0] -> TypeError: 'set' object is not subscriptable
a = set("jooooaoooo")
print(a)
print("a" in a, "J" not in a)
print({1, 2, 3, 4} == {4, 4, 1, 2, 3})  # True

# operações
c1 = {1, 2}
c2 = {3, 4}
print(c1.union(c2))
print(c1.intersection(c2))
# c1.update(c2)
print(c2 <= c1)
print(c1 >= c2)
# TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print({1, 2, 3, 4} + {4})
print({1, 2, 3, 4} - {4})
c1 -= c2
print(c1)
