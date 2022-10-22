from math import cos, sin, sqrt, ceil
import svg, sys

# Amount of points to draw
POINTS = 100_000

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

output_image = svg.SVG(1000, 1000)

for n in range(0, POINTS):
    x, y  = convert_to_spiral(n)

    mapped = compiled(n)
    prime = is_prime(mapped)

    point = svg.SVG_Circle(x + 500, y + 500, 1, fill = 'black' if prime else 'white')

    output_image.append(point) 
    if not (n % 10): print(f'{n/POINTS * 100}%')

output_image.save(file_name)