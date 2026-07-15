x = 1
y = 3
z = 4

a = x + y
print(a) 
a = x - y 
print(a)
a = x * y 
print(a)
a = x ** y 
print(a)
a = x / y 
print(a)
a = x + (y * z)
print(a)

40 + 32.3

a = int(2.4)

print(1 < 2)

print(5.0 == 5.0 )

print(4.0 != 5.0)

print(x, y, z)

print(x > y and y < z)


import math

print(math.floor(3.4))

print(math.floor(-3.4))

print(math.trunc(2.5))
print(math.trunc(-2.5))

print(99999999999 * 2.1)

print(0o20)#octal
print(0xFF)#hexa
print(0b1000)#binary


x = 1

print(x << 2)
print(x >> 2)

import random

print(random.randint(1,100))
print(random.randint(1,100))

l1 = ['a', 'b', 'c', 'd', 'e' ]
print(random.choice(l1))

random.shuffle(l1)
print(l1)


print(0.1 + 0.1 + 0.1)

print(0.1 + 0.1 + 0.1 - 0.3)

print((0.1 + 0.1 + 0.1) - 0.3)

from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1'))

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6}

print(set1 & set2)
print(set1 | set2)


print(type(True))
print(True == 1)

