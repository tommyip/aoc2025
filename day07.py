from functools import cache

with open("inputs/day07.txt") as f:
    lines = f.read().strip().split("\n")[::2]

starter_beam = lines[0].index("S")
beams = {starter_beam}
manifold = [{i for i, tachyon in enumerate(line) if tachyon == "^"} for line in lines[1:]]

part1 = 0
for splitters in manifold:
    new_beams = set()
    for beam in beams:
        if beam in splitters:
            part1 += 1
            new_beams |= {beam - 1, beam + 1}
        else:
            new_beams.add(beam)
    beams = new_beams

print(part1)


@cache
def timelines(beam, depth):
    if depth == len(lines) - 1:
        return 1
    if beam in manifold[depth]:
        return timelines(beam - 1, depth + 1) + timelines(beam + 1, depth + 1) 
    return timelines(beam, depth + 1)

print(timelines(starter_beam, 0))
