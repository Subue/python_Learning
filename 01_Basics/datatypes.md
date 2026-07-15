# Python Data Types (Detailed Notes)

## Introduction

A **data type** defines what kind of value a variable stores and what
operations can be performed on it.

``` python
x = 10
name = "Subodh"
pi = 3.14
```

Use `type()` to check a variable's type:

``` python
x = 10
print(type(x))   # <class 'int'>
```

------------------------------------------------------------------------

# 1. Numeric Data Types

## int

Stores whole numbers.

``` python
a = 100
b = -25
```

Operations: `+ - * / // % **`

## float

Stores decimal numbers.

``` python
price = 99.99
```

## complex

Stores complex numbers.

``` python
z = 3 + 4j
print(z.real)
print(z.imag)
```

------------------------------------------------------------------------

# 2. String (`str`)

Strings store text.

``` python
name = "Python"
```

Common operations:

``` python
print(name.upper())
print(name.lower())
print(len(name))
print(name[0])
print(name[0:3])
```

Strings are **immutable**.

------------------------------------------------------------------------

# 3. Boolean (`bool`)

Represents logical values.

``` python
a = True
b = False
```

Used in conditions:

``` python
age = 18
print(age >= 18)
```

------------------------------------------------------------------------

# 4. List

Ordered, mutable collection.

``` python
fruits = ["Apple", "Banana", "Mango"]
fruits.append("Orange")
fruits[0] = "Grapes"
```

Methods: - append() - insert() - remove() - pop() - sort() - reverse()

------------------------------------------------------------------------

# 5. Tuple

Ordered, immutable collection.

``` python
point = (10, 20)
```

Useful for fixed data.

------------------------------------------------------------------------

# 6. Set

Unordered collection of unique values.

``` python
nums = {1,2,3,3}
print(nums)
```

Methods: - add() - remove() - union() - intersection()

------------------------------------------------------------------------

# 7. Dictionary

Stores key-value pairs.

``` python
student = {
    "name": "Subodh",
    "age": 21,
    "marks": 90
}
print(student["name"])
```

Methods: - keys() - values() - items() - get() - update()

------------------------------------------------------------------------

# 8. Range

``` python
for i in range(1,6):
    print(i)
```

------------------------------------------------------------------------

# 9. Binary Types

## bytes

``` python
b = b"Hello"
```

## bytearray

``` python
ba = bytearray(5)
```

## memoryview

``` python
mv = memoryview(b"Hello")
```

------------------------------------------------------------------------

# 10. NoneType

``` python
value = None
```

Represents no value.

------------------------------------------------------------------------

# Mutable vs Immutable

  Mutable     Immutable
  ----------- -----------
  list        int
  dict        float
  set         bool
  bytearray   str
              tuple
              bytes
              frozenset

------------------------------------------------------------------------

# Summary

  Type         Example              Mutable
  ------------ -------------------- ---------
  int          10                   No
  float        3.14                 No
  complex      2+3j                 No
  bool         True                 No
  str          "Hello"              No
  list         \[1,2\]              Yes
  tuple        (1,2)                No
  set          {1,2}                Yes
  frozenset    frozenset({1,2})     No
  dict         {"a":1}              Yes
  bytes        b"abc"               No
  bytearray    bytearray(5)         Yes
  memoryview   memoryview(b"abc")   Depends
  NoneType     None                 No

## Interview Questions

1.  What is the difference between List and Tuple?
2.  What is the difference between Set and Dictionary?
3.  What is mutable and immutable?
4.  Difference between `==` and `is`?
5.  What does `type()` do?
6.  Why are strings immutable?
