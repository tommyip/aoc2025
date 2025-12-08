from math import prod
from itertools import combinations

with open("inputs/day08.txt") as f:
    lines = f.read().strip().split("\n")

boxes = [tuple(map(int, line.split(","))) for line in lines]
dists = sorted(combinations(boxes, 2), key=lambda ab: sum((ai - bi) ** 2 for ai, bi in zip(*ab)))

circuits = []
for i, (a, b) in enumerate(dists):
    ac = None
    bc = None
    for circuit in circuits:
        if a in circuit:
            ac = circuit
        if b in circuit:
            bc = circuit

    if ac is not None and bc is not None:
        if ac is not bc:
            circuits.remove(bc)
            ac |= bc
    elif ac is not None:
        ac.add(b)
    elif bc is not None:
        bc.add(a)
    else:
        circuits.append({a, b})

    if i == 999:
        print(prod(sorted(map(len, circuits), reverse=True)[:3]))

    if len(circuits[0]) == len(boxes):
        print(a[0] * b[0])
        break
