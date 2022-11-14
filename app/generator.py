from math import ceil, sqrt
from ctypes import CDLL

def is_prime(x):
    for i in range(2, 1 + ceil(sqrt(x))):
        if (x % i == 0): return x == 2
    if x == 0 or x == 1: return False
    return True


class Generator:

    def __init__(self) -> None:
        self.func = 



def next_point(prev: tuple[float, float], heading: tuple[float, float] = (1, 0)):
    x, y = prev = (prev[0] + heading[0], prev[1] + heading[1])
    if   (x - 1 == -y) and y < 1: heading = (0 ,  1)
    elif (x     == y) and x > 0: heading = (-1,  0)
    elif (-x    == y) and y > 0: heading = (0 , -1)
    elif (x     == y) and x < 0: heading = (1 ,  0)

    return prev, heading

def get_spiral(func, start: int = 0, stop: int = 100_000):

    output_datapoints = {}

    point = (0, 0)
    heading = (1, 0)

    for n in range(start, stop):
        mappped = func(n)
        prime = is_prime(mappped)
        if prime:
            entry = f'{point[0]};{point[1]}'
            output_datapoints[entry] = prime

        point, heading = next_point(point, heading)

    return output_datapoints
