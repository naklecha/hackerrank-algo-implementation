#!/bin/python

import sys


n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
   grid_t = str(raw_input().strip())
   grid.append(grid_t)
for i in range(1,len(grid)-1):
    for j in range(1,len(grid[0])-1):
        if grid[i][j] > grid[i+1][j] and grid[i][j] > grid[i][j+1] and grid[i][j] > grid[i-1][j] and grid[i][j] > grid[i][j-1]:
            grid[i] = grid[i][:j] + "X" + grid[i][j+1:]

for k in grid:
    print k
