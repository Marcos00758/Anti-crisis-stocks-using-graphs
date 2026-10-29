def generator():
    yield 1
    print("A")
    yield 2
    print("B")
    yield 3
    print('C')
    return n

g = generator()

print(next(g))
print(next(g))


'''for n in g:
    print(n)'''