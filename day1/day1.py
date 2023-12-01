import re
from collections import namedtuple

# STRUCTURES
d = {
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
d2 = {}
for i in d.items():
    d2[i[0][::-1]] = i[1]

# CONSTANTS
FILENAME = "input.txt"

# GLOBALS


# FILE PARSING


# HELPERS


# MAIN
def part1() -> int:
    sum = 0
    # with open(FILENAME) as f:
    #     for line in f:
    #         nums = re.findall(r'\d', line)
    #         sum += int(nums[0] + nums[-1])
    return sum


def part2() -> int:
    sum = 0
    with open(FILENAME) as f:
        for line in f:
            first = re.search(r'\d|one|two|three|four|five|six|seven|eight|nine', line).group()
            if len(first) > 1:
                first = str(d[first])
            second = re.search(r'\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', line[::-1]).group()
            if len(second) > 1:
                second = str(d2[second])
            sum += int(first + second)

            # nums = []
            # digits = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
            # for s in digits:
            #     if len(s) > 1:
            #         nums.append(str(d[s]))
            #     else:
            #         nums.append(s)
            # sum += int(nums[0] + nums[-1])
            print(first, second)
    return sum


print("Part 1: " + str(part1()))
print("Part 2: " + str(part2()))
