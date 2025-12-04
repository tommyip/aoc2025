from itertools import count

with open("inputs/day04.txt") as f:
    lines = f.read().strip().split("\n")

grid = {complex(i, j) for j, line in enumerate(lines) for i, cell in enumerate(line) if cell == "@"}
neighbors = [-1-1j, -1j, 1-1j, -1+0j, 1+0j, -1+1j, 1j, 1+1j]

part2 = 0
for epoch in count(0):
    remove = set()
    for cell in grid:
        if sum(cell + dir in grid for dir in neighbors) < 4:
            remove.add(cell)
    if not remove:
        break
    if epoch == 0:
        print(len(remove))
    part2 += len(remove)
    grid -= remove

print(part2)
