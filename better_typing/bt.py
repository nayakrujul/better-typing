class Union:
    def __init__(self, type1, type2):
        if not isinstance(type1, (type, Type)) or not isinstance(type2, (type, Type)):
            raise ValueError(f'{type1!r}, {type2!r} are not types')
        self.types = type1, type2
    def __str__(self):
        return self.types[0].__name__ + ' | ' + self.types[1].__name__
    @property
    def __name__(self):
        return str(self)

class Type:
    def __init__(self, dtype, of=None):
        if isinstance(dtype, Type):
            self.dtype = dtype.dtype
        elif isinstance(dtype, (type, Union)):
            self.dtype = dtype
        else:
            raise ValueError(f'{dtype!r} is not a type')
        if of is not None and not isinstance(of, (Type, Union, type)):
            raise ValueError(f'{of!r} is not a type')
        self.of = of
    def __str__(self):
        if self.of is not None:
            return f'{self.dtype.__name__}[{str(self.of.__name__)}]'
        else:
            return str(self.dtype.__name__)
    def __getitem__(self, cls):
        return Type(self, cls)
    def __or__(self, other):
        return Union(self, other)
    def __ror__(self, other):
        return Union(other, self)
    @property
    def __name__(self):
        return str(self)

def IsInstance(obj, dtype):
    if isinstance(dtype, type):
        return isinstance(obj, dtype)
    elif isinstance(dtype, Type):
        if dtype.of is None:
            return isinstance(obj, dtype.dtype)
        return all(IsInstance(item, dtype.of) for item in obj)
    elif isinstance(dtype, Union):
        return any(IsInstance(obj, t) for t in dtype.types)

Bool = Type(bool)
Dict = Type(dict)
Float = Type(float)
Int = Type(int)
List = Type(list)
Set = Type(set)
Str = Type(str)
Tuple = Type(tuple)
