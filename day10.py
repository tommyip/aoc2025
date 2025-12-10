from collections import deque

from z3 import Int,  Sum, Optimize

with open("inputs/day10.txt") as f:
    lines = f.read().strip().split("\n")


part1 = 0
for line in lines:
    pattern, *buttons = line.split(" ")
    target = 0
    for x in reversed(pattern[1:-1]):
        target <<= 1
        if x == "#":
            target += 1
    buttons = [[int(x) for x in button[1:-1].split(",")] for button in buttons[:-1]]
    options = []
    for button in buttons:
        x = 0
        for bit in button:
            x |= 1 << bit
        options.append(x)

    min_press = None
    q = deque([(0, 0)])
    while len(q):
        cur, press = q.popleft()
        if cur == target:
            if min_press and press < min_press or not min_press:
                min_press = press
            continue

        if min_press is not None and press < min_press or min_press is None:
            for option in options:
                q.append((cur ^ option, press + 1))

    part1 += min_press

print(part1)

part2 = 0
for line in lines:
    pattern, *buttons = line.split(" ")
    buttons = [[int(x) for x in button[1:-1].split(",")] for button in buttons]
    buttons, targets = buttons[:-1], buttons[-1]

    eqs = []
    vars = [Int(f"x{k}") for k in range(len(buttons))]
    for i, target in enumerate(targets):
        lhs = [var for var, button in zip(vars, buttons) if i in button]
        eqs.append(Sum(lhs) == target)
    constraints = [var >= 0 for var in vars]

    s = Optimize()
    ans = Int("ans")
    s.add(*eqs, *constraints, Sum(vars) == ans)
    s.minimize(ans)
    s.check()
    m = s.model()
    part2 += m[ans].as_long()

print(part2)
