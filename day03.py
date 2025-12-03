with open("inputs/day03.txt") as f:
    lines = [list(map(int, line)) for line in f.read().strip().split("\n")]

def joltage(nums, n):
    digits = []
    start = 0
    for i in range(n):
        subnums = nums[start:len(nums) - n + 1 + i]
        x = max(subnums)
        digits.append(x)
        start += subnums.index(x) + 1
    return int("".join(map(str, digits)))

print(sum(joltage(nums, 2) for nums in lines))
print(sum(joltage(nums, 12) for nums in lines))
