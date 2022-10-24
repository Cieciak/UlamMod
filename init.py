from math import cos, sin, sqrt, ceil
import svg, sys


# Try to get function from command
try: user_function = sys.argv[1]
except IndexError: user_function = None
# Try to get filename from command
try: file_name = sys.argv[2]
except IndexError: file_name = None
# Try to get amount from command
try: points = int(sys.argv[3])
except IndexError: points = 100_000
except ValueError:points = 100_000

# Ask user for the function
if not user_function: user_function = input("Enter f(n): ℕ → X, n ∈ ℕ: ")
print(user_function)
compiled = lambda n: eval(compile(user_function, './err', 'eval'))

# Determine the output filename
if not file_name: file_name = input("Enter filename: ")
if not file_name: file_name = f'{user_function}.svg'.replace(' ', '_')

def convert_to_spiral(n: int, *, power: float = 0.5, scale: float = 1) -> tuple[float, float]:
    x = n ** power * cos(n)
    y = n ** power * sin(n)
    return x, y

def is_prime(x):
    for i in range(2, ceil(sqrt(x))):
        if (x % i == 0): return False
    return True

def next_point(prev: tuple[float, float], heading: tuple[float, float] = (1, 0)) -> tuple[float, float]:
    x, y = prev = (prev[0] + heading[0], prev[1] + heading[1])
    if   (x - 1 == -y) and y < 1: heading = (0 ,  1)
    elif (x     == y) and x > 0: heading = (-1,  0)
    elif (-x    == y) and y > 0: heading = (0 , -1)
    elif (x     == y) and x < 0: heading = (1 ,  0)

    return prev, heading

output_image = svg.SVG(250, 250)

h, w = output_image.heigth, output_image.width
point = (0, 0)
heading = (1, 0)

for n in range(0, points):
    x, y  = point

    mapped = compiled(n)
    prime = is_prime(mapped)

    #dot = svg.SVG_Circle(x + 500, y + 500, .5, fill = 'black' if prime else 'white')
    dot = svg.SVG_Rect(x - .5 + 0.5 * w, y - .5 + 0.5 * h, 1, 1, fill = 'black' if prime else 'white')

    output_image.append(dot) 

    point, heading = next_point(point, heading)

    if not (n % 10): print(f'{round(n/points * 100, 2)}%')

output_image.save(file_name)