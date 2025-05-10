print("name : monalisa.n \n usn : 1AY24AI073 \n section : O ")

import time, random, os

def display(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(''.join('█' if cell else ' ' for cell in row))

def next_gen(grid):
    def count(x, y):
        return sum(grid[i][j]
                   for i in range(x-1, x+2)
                   for j in range(y-1, y+2)
                   if (i, j) != (x, y) and 0 <= i < h and 0 <= j < w)
    return [[1 if (cell and 2 <= count(x, y) <= 3) or (not cell and count(x, y) == 3) else 0
             for y, cell in enumerate(row)] for x, row in enumerate(grid)]

w, h = 20, 10
grid = [[random.randint(0, 1) for _ in range(w)] for _ in range(h)]

try:
    while True:
        display(grid)
        grid = next_gen(grid)
        time.sleep(0.3)
except KeyboardInterrupt:
    print("Game stopped.")
