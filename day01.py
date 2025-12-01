with open("inputs/day01.txt") as f:
    lines = f.read().strip().split("\n")

pos = 50
part1, part2 = 0, 0

for line in lines:
    dir, dist = line[0], int(line[1:])
    for _ in range(dist):
        if dir == "L":
            pos = (pos - 1) % 100
        else:
            pos = (pos + 1) % 100
        if pos == 0:
            part2 += 1
    part1 += pos == 0
  
print(part1)
print(part2)
