def dot(x):
    return 3*x+5

#map2 = [dot(x) for x in range(10)]
#print(map2)

def map2(func, *iterables):
    for x in range(*iterables):
        yield func(x)

test = map2(dot, 10)
print(next(test))
print(next(test))
print(list(test))