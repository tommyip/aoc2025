with open('inputs/day05.txt') as f:
    ranges, ids = [x.split("\n") for x in  f.read().strip().split("\n\n")]

fresh = []
for line in ranges:
    a, b = line.split("-")
    fresh.append((int(a), int(b)))


print(sum(any(lo <= int(x) <= hi for lo, hi in fresh) for x in ids))

part2 = 0
while fresh:
    fresh.sort()
    lo, hi = fresh.pop(0)
    changed = False
    for i, (lo1, hi1) in enumerate(fresh):
        if lo1 <= hi:
            if lo1 > lo:
                fresh.append((lo, lo1 - 1))
            changed = True
        if hi >= hi1:
            if hi > hi1:
                fresh.append((hi1 + 1, hi))
            changed = True
        if changed:
            break
    else:
        part2 += hi - lo + 1
        continue
        

print(part2)
