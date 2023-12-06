import re


# STRUCTURES


# GLOBALS


# MAIN
def do_map(nums, ranges):
    for i in range(len(nums)):
        for rang in ranges:
            if rang[1] <= nums[i] < rang[1] + rang[2]:
                nums[i] = rang[0] - rang[1] + nums[i]
                break


def part1(lines) -> int:
    nums = list(map(int, re.findall(r'\d+', lines[0])))
    return lowest_seed(nums, lines)


def lowest_seed(nums, lines):
    ranges = []
    i = 3
    while i < len(lines):
        if lines[i] == '\n':
            print(i)
            do_map(nums, ranges)
            ranges = []
            i += 2
        else:
            ranges.append(tuple(map(int, re.findall(r'\d+', lines[i]))))
            i += 1
    do_map(nums, ranges)
    return min(nums)


def part2(lines) -> int:
    nums = list(map(int, re.findall(r'\d+', lines[0])))
    seeds = []
    for i in range(0, len(nums), 2):
        seeds.extend(range(nums[i], nums[i] + nums[i+1]))
    return lowest_seed(seeds, lines)


def main():
    with open("test.txt") as f:
        lines = f.readlines()
        print("Part 1 Test: " + str(part1(lines)))
        print("Part 2 Test: " + str(part2(lines)))
    with open("input.txt") as f:
        lines = f.readlines()
        print("Part 1 Input: " + str(part1(lines)))
        print("Part 2 Input: " + str(part2(lines)))


if __name__ == '__main__':
    main()
