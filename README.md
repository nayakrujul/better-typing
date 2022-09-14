# better-typing
A better version of typing in Python.

## Installation

From PyPI:

```zsh
$ pip install better-python
```

## Usage

### Import module

You can import the `better_typing` module

```python
from better_typing import *
```

### Constants

The module has type alias constants, like `typing`:

```python
print(Bool)  # bool
print(Dict)  # dict
print(Float) # float
print(Int)   # int
print(List)  # list
print(Set)   # set
print(Str)   # str
print(Tuple) # tuple
```

These are all subscriptable:

```python
print(List[int])               # list[int]
print(Tuple[str])              # tuple[str]
print(Set[List[Tuple[float]]]) # set[list[tuple[float]]]
```

### Creating custom type aliases

Let's create a class, `MyClass`:

```python
class MyClass:
    def __init__(self, x):
        self.x = x
```

We can then create an alias for `MyClass` by using `Type`:

```python
MC = Type(MyClass)
print(MC)      # MyClass
print(MC[int]) # MyClass[int]
```

### Unions

The `better_typing` way of creating a union is by using `|`:

```python
print(List | Tuple)                   # list | tuple
print(List[Int | Float])              # list[int | float]
print(List[Int | Float] | Tuple[Str]) # list[int | float] | tuple[str]
```

Note: you can also use `Union(Int, Float)`, but this is not recommended.

### Instance Checks

`better_typing` has a function for replacing `isinstance`:

```python
l = [1, 2, 3]
print(IsInstance(l, List[int]))   # True
print(IsInstance(l, List[float])) # False
```

You can use unions with this as well:

```python
l = [1, 1.1, 1.2]
print(IsInstance(l, List[int]))         # False
print(IsInstance(l, List[float]))       # False
print(IsInstance(l, List[Int | Float])) # True
```
