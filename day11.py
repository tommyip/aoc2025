from cachetools import cached
from cachetools.keys import hashkey

from collections import defaultdict

with open("inputs/day11.txt") as f:
    lines = f.read().strip().split("\n")

network = {}
inetwork = defaultdict(list)
for line in lines:
    src, *dests = line.replace(":", "").split()
    network[src] = dests
    for dest in dests:
        inetwork[dest].append(src)

@cached(cache={}, key=lambda s, d, _: hashkey(s, d))
def dfs(src, dst, network):
    if src == dst:
        return 1
    return sum(dfs(nei, dst, network) for nei in network.get(src, []))

print(dfs("you", "out", network))

# Part 2 - len(svr -> fft) * len(fft -> dac) * len(dac -> out)

@cached(cache={})
def dfs_paths(device, dir, history):
    if device == "svr" or device == "out":
        return {history}
    histories = set()
    net = network if dir else inetwork
    for nei in net[device]:
        if nei not in history:
            histories |= dfs_paths(nei, dir, history + (nei,))
    return histories

fft_left = dfs_paths("fft", False, ())
dac_right = dfs_paths("dac", True, ())

unreachable = set()
for path in fft_left | dac_right:
    unreachable |= set(path)

pruned_network = {}
for key, neis in network.items():
    if key not in unreachable:
        if neis_ := [nei for nei in neis if nei not in unreachable]:
            pruned_network[key] = neis_

fft_to_dac = dfs("fft", "dac", pruned_network)

print(fft_to_dac * len(fft_left) * len(dac_right))
