import re

# STRUCTURES

# CONSTANTS
FILENAME = "input.txt"

# GLOBALS
numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
reverse_numbers = {}
for s in numbers.keys():
    reverse_numbers[s[::-1]] = numbers[s]

# FILE PARSING
with open(FILENAME) as f:
    lines = f.readlines()

# HELPERS


# MAIN
def part1() -> int:
    rsf = 0
    for line in lines:
        nums = re.findall(r'\d', line)
        rsf += int(nums[0] + nums[-1])
    return rsf


def part2() -> int:
    rsf = 0
    pattern = r'\d|' + '|'.join(list(numbers.keys()))
    reverse_pattern = r'\d|' + '|'.join(list(reverse_numbers.keys()))
    for line in lines:
        first = re.search(pattern, line).group()
        if len(first) > 1:
            first = str(numbers[first])
        second = re.search(reverse_pattern, line[::-1]).group()
        if len(second) > 1:
            second = str(reverse_numbers[second])
        rsf += int(first + second)
    return rsf


print("Part 1: " + str(part1()))
print("Part 2: " + str(part2()))
