# print(1.1 + 2.2)  -> 3.3000000000000003 -> binários
import decimal
from decimal import Decimal, getcontext
print(Decimal(1) / Decimal(2))
getcontext().prec = 10
print(Decimal(1) / Decimal(7))
print(Decimal.max(Decimal(1), Decimal(7)))
print(dir(Decimal))
print(Decimal(1.1) + Decimal(2.2))
print(dir(decimal))
print(dir())
