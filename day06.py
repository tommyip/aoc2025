import math
import re

with open("inputs/day06.txt") as f:
    lines = f.read().strip("\n").split("\n")

ops = [{"+": sum, "*": math.prod}[op] for op in lines[-1].replace(" ", "")]

def part(groups):
    print(sum([op(group) for op, group in zip(ops, groups)]))

elems = [map(int, re.sub(r"\s+", " ", line).split()) for line in lines[:-1]]
elems = list(map(list, zip(*elems)))
part(elems)


rotated = ["".join(l).strip() for l in list(map(list, zip(*lines[:-1])))]
groups = [[]]
for num in rotated:
    if num == "":
        groups.append([])
    else:
        groups[-1].append(int(num))

part(groups)
