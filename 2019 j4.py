flip = list(input())
grid = [1,2,3,4]
for current in flip:
    if current == "H":
        grid[0], grid[2] = grid[2], grid[0]
        grid[1], grid[3] = grid[3],grid[1]
    elif current == "V":
        grid[0], grid[1] = grid[1], grid[0]
        grid[2], grid[3] = grid[3],grid[2]

for row in range(len(grid)):
    print(' '.join(grid[row]))