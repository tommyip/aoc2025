from math import copysign
from itertools import pairwise, combinations

with open("inputs/day09.txt") as f:
    lines = f.read().strip().split("\n")

reds = [tuple(map(int, l.split(","))) for l in lines]

edges = set()
for a, b in pairwise(reds + [reds[0]]):
    dx, dy = b[0] - a[0], b[1] - a[1]
    dir = int(copysign(min(abs(dx), 1), dx)), int(copysign(min(abs(dy), 1), dy))
    while a != b:
        edges.add(a)
        a = a[0] + dir[0], a[1] + dir[1]
    edges.add(b)

part1 = 0
part2 = 0

for (ax, ay), (bx, by) in combinations(reds, 2):
    width, height = abs(ax - bx) + 1, abs(ay - by) + 1
    area = width * height
    part1 = max(part1, area)
    x0, x1 = min(ax, bx) + 1, max(ax, bx) - 1
    y0, y1 = min(ay, by) + 1, max(ay, by) - 1
    if x1 < x0 or y1 < y0 or area < part2:
        continue
    for x, y in edges:
        if x0 <= x <= x1 and y0 <= y <= y1:
            break
    else:
        part2 = max(part2, area)

print(part1)
print(part2)
