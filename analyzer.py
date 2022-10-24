import numpy as np
from PIL import Image
from math import *

def load(path):

    with open(path) as file:
        ulam_data = np.loadtxt(file, delimiter=',')
    
    points = []
    x, y, *_ = ulam_data[-1]
    offset = int(max(abs(x), abs(y)))
    for row in ulam_data:
        x, y, prime = row
        points.append([(int(x) + offset, int(y) + offset), prime])

    return points, 2 * offset +1

if __name__ == '__main__':
    p, x = load('out.csv')

    grid = np.zeros((x, x), dtype = int)

    for entry, flag in p:
        grid[entry] = flag

    row_sum = np.sum(grid, axis=1)

    print(row_sum * 0.01)

    row_sum = np.reshape(row_sum, [1, -1])
    for _ in range(4):
        row_sum = np.append(row_sum, row_sum, axis=0)
    img = Image.fromarray(255*row_sum * 0.01)
    img = img.convert('RGB')
    #img = Image.fromarray(grid.T)
    img.save('out.png')