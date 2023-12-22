import functools
import re


# STRUCTURES


# GLOBALS


# MAIN
@functools.cache
def valid(springs, nums):
    springs = springs.replace('?', '.')
    groups = re.split(r'[.]+', springs)
    nums_idx = 0
    for group in groups:
        if len(group) != 0:
            if nums_idx == len(nums) or len(group) != nums[nums_idx]:
                return False
            nums_idx += 1
    return True


@functools.cache
def num_combinations(springs: str, nums: tuple, nums_idx: int, springs_idx: int) -> int:
    # iterate through line, placing first group in all possible positions, then recursing
    # keep track of past index allowed to place the next group

    # starting from idx, iterate forward to find all places to put next group, replacing ? with .
    # each time position is found, recurse with that ? replaced and the rest of nums

    # base case: no nums left
    if nums_idx == len(nums):
        if valid(springs, nums):
            # print(springs.replace('?', '.'))
            return 1
        return 0
    # try to place in all spots
    n = nums[nums_idx]
    rsf = 0
    for start in range(springs_idx, len(springs) - n + 1):
        end = start + n
        area = springs[start:end]
        if area.replace('?', '#') != '#' * n:
            # invalid area
            continue
        if end >= len(springs):
            # next is off edge
            if nums_idx == len(nums) - 1 and (start - 1 < 0 or springs[start-1] in '?.'):
                # used last num, finished combo (if valid)
                new_springs = springs[:start].replace('?', '.') + '#' * n
                if valid(new_springs, nums):
                    # print(new_springs)
                    rsf += 1
            continue
        if springs[end] in '?.' and (start - 1 < 0 or springs[start-1] in '?.'):
            # valid area, place group here
            new_springs = springs[:start] + '#' * n + '.' + springs[end+1:]
            rsf += num_combinations(new_springs, nums, nums_idx + 1, end+1)
    return rsf


def part1(lines) -> int:
    rsf = 0
    for line in lines:
        springs, nums = line.strip().split()
        nums = tuple(map(int, nums.split(',')))
        combos = num_combinations(springs, nums, 0, 0)
        print(combos)
        # print()
        rsf += combos
    return rsf


def unfold(line):
    springs, nums = line.split()
    new_springs = springs
    new_nums = nums
    for _ in range(4):
        new_springs += '?' + springs
        new_nums += ',' + nums
    return new_springs + ' ' + new_nums


def part2(lines) -> int:
    for i, line in enumerate(lines):
        lines[i] = unfold(line.strip())
    return part1(lines)


def main():
    with open("test.txt") as f:
        lines = f.readlines()
        print("Part 1 Test: " + str(part1(lines)))
        # print("Part 2 Test: " + str(part2(lines)))
    with open("input.txt") as f:
        lines = f.readlines()
        # print("Part 1 Input: " + str(part1(lines)))
        print("Part 2 Input: " + str(part2(lines)))


if __name__ == '__main__':
    main()
