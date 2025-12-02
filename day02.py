from itertools import batched

with open("inputs/day02.txt") as f:
    lines = f.read().strip().split(",")


part1 = 0
part2 = set()
for line in lines:
    lo, hi = [int(x) for x in line.split("-")]
    for x in range(lo, hi + 1):
        xs = str(x)
        for n in range(2, len(xs) + 1):
            if len(xs) % n == 0:
                if len(set(batched(xs, len(xs) // n))) == 1:
                    if n == 2:
                        part1 += x
                    part2.add(x)

print(part1)
print(sum(part2))
