def szukajWLiscie(a, lista):
    if isinstance(a, (int, float)):
        return a in lista
    elif isinstance(a, str):
        if a.isdigit():
            return int(a) in lista
        else:
            suma = sum(ord(char) for char in a)
            return suma in lista
    elif isinstance(a, bool):
        return int(a) in lista
    else:
        raise TypeError(f"Nieobsługiwany typ: {type(a)}")


print(szukajWLiscie(42, [10, 20, 42, 100]))

print(szukajWLiscie(42.0, [10, 20, 42.0, 100]))

print(szukajWLiscie("42", [10, 20, 42, 100]))

print(szukajWLiscie("abc", [294]))


print(szukajWLiscie(True, [0, 1, 2]))

try:
    print(szukajWLiscie([1, 2], [10, 20, 42]))
except TypeError as e:
    print(e)
