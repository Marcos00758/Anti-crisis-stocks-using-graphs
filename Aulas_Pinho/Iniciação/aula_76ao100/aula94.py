lista = [1,2,3,4,5]

def gen():
    yield from lista
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6

g = gen()

print(next(g))