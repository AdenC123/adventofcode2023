import functools
import re


# STRUCTURES


# GLOBALS


# MAIN
@functools.cache
def possible(springs, nums):
    # if all ? are not springs, is it possible to complete?
    springs = springs.replace('?', '.')
    groups = re.split(r'[.]+', springs)
    groups = [g for g in groups if len(g) != 0]
    for group in groups:
        if len(group) not in nums:
            return False
    return True


@functools.cache
def valid(springs, nums):
    # assume no ? in springs
    groups = re.split(r'[.]+', springs)
    groups = [g for g in groups if len(g) != 0]
    if len(nums) != len(groups):
        return False
    for n, group in zip(nums, groups):
        if len(group) != n:
            return False
    return True


@functools.cache
def num_combinations(springs: str, nums: tuple) -> int:
    # base case: all springs placed and valid
    # if not possible(springs, nums):
    #     return 0
    if '?' not in springs:
        if valid(springs, nums):
            return 1
        return 0
    # place a spring and a dot in the first slot and recurse
    num_dot = num_combinations(springs.replace('?', '.', 1), nums)
    num_spring = num_combinations(springs.replace('?', '#', 1), nums)
    return num_dot + num_spring


def part1(lines) -> int:
    rsf = 0
    for line in lines:
        springs, nums = line.strip().split()
        nums = tuple(map(int, nums.split(',')))
        combos = num_combinations(springs, nums)
        print(combos)
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
        # print("Part 1 Test: " + str(part1(lines)))
        print("Part 2 Test: " + str(part2(lines)))
    with open("input.txt") as f:
        lines = f.readlines()
        # print("Part 1 Input: " + str(part1(lines)))
        # print("Part 2 Input: " + str(part2(lines)))


if __name__ == '__main__':
    main()
