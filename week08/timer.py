from time import time
from time import sleep

def timer(func):
    def func_wrapper(*args, **kargs):
        time_start = time()
        result = func(*args, **kargs)
        time_end = time()
        time_spend = time_end - time_start
        print('%s cost time: %.3f s' % (func.__name__, time_spend))
        return result
    return func_wrapper

@timer
def test(x):
    calc=0
    for i in range(x):
        calc += i
        sleep(0.1)
    return calc

print(test(10))


@timer
def go(*args):
    for i in args:
        print(i)

print(go(1,2,3,5,7,8,9))