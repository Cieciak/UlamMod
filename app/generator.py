from math import ceil, sqrt
from types import FunctionType

csqrt = lambda n: ceil(sqrt(n))

class Generator:

    @staticmethod
    def is_prime(n: int) -> bool:
        if n < 2: return False 
        for i in range(2, 1 + csqrt(n)): 
            if (n % i == 0): return n == 2
        return True 

    @staticmethod
    def next_point(prev: tuple[float, float], heading: tuple[float, float]):
        x, y = prev = (prev[0] + heading[0], prev[1] + heading[1])
        if   (x - 1 == -y) and y < 1: heading = ( 0,  1)
        elif (x     ==  y) and x > 0: heading = (-1,  0)
        elif (-x    ==  y) and y > 0: heading = ( 0, -1)
        elif (x     ==  y) and x < 0: heading = ( 1,  0)

        return prev, heading

    def __init__(self) -> None:
        self.func: FunctionType = Generator.is_prime

    def bind_function(self, func: FunctionType): self.func = func

    def get_spiral(self, func: FunctionType, start: int = 0, stop: int = 100_000):
        output_datapoints = {}

        point = (0, 0)
        heading = (1, 0)

        for n in range(start, stop):
            mapped = func(n)
            prime = self.func(mapped)
            if prime: 
                entry = f'{point[0]};{point[1]}'
                output_datapoints[entry] = prime

            point, heading = Generator.next_point(point, heading)

        return output_datapoints

    def test(self, *, n = 100):
        '''Will test the function for first n numbers'''
        for x in range(n):
            print(f'{x}: {self.func(x)}')

if __name__ == '__main__':
    pass