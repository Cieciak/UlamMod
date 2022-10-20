from math import cos, sin, sqrt, ceil

text = r'<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400">'

def pos_to_place(i):
    power = 0.51
    x = i**power * cos(i)
    y = i**power * sin(i)

    return x, y

def f(x):
    return 6 * x + 5

def is_prime(x):
    for i in range(2, x):
        if (x % i == 0): return False
    return True

def draw_circle(x, y, i):
    return f'<circle cx="{200 + x}" cy="{200 + y}" r="1" fill="{"black" if is_prime(i) else "white"}"/>\n'

for j in range(10_000):
    text += draw_circle(*pos_to_place(j), f(j))

text += r'</svg>'

print(text)