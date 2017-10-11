# Enter your code here. Read input from STDIN. Print output to STDOUT
def bomb(r, c, grid, t):
    complete_grid = [ ["O"]*c for i in range(r) ]
    stable_grid = [ ["O"]*c for i in range(r) ]
    other_grid = [ ["O"]*c for i in range(r) ]
    for i in range(r):
        for j in range(c):
            if grid[i][j] == "O":
                other_grid[i][j] = "."
                if i>0:
                    other_grid[i-1][j] = "."
                if j>0:
                    other_grid[i][j-1] = "."
                if i<r-1:
                    other_grid[i+1][j] = "."
                if j<c-1:
                    other_grid[i][j+1] = "."
    for i in range(r):
        for j in range(c):
            if other_grid[i][j] == "O":
                stable_grid[i][j] = "."
                if i>0:
                    stable_grid[i-1][j] = "."
                if j>0:
                    stable_grid[i][j-1] = "."
                if i<r-1:
                    stable_grid[i+1][j] = "."
                if j<c-1:
                    stable_grid[i][j+1] = "."
    #print grid
    #print complete_grid
    #print other_grid
    if t==0 or t==1:
        return grid
    if (t-1)%2==0 and not (t-1)%4==0:
        return other_grid
    if (t-1)%4==0:
        return stable_grid
    if t%2==0:
        return complete_grid
grid = []
r, c, t = map(int, raw_input().split())
for _ in range(r):
    row = [ l for l in raw_input() ]
    grid.append(row)
res = "\n".join([ "".join(line) for line in bomb(r, c, grid, t) ]) 
print res
