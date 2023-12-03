import re


# STRUCTURES


# GLOBALS


# HELPERS


# MAIN
def is_part(num: str, i: int, row: int, lines) -> bool:
    for x in range(i-1, i+len(num)+1):
        if x < 0 or x >= len(lines[0].strip()):
            continue
        for y in range(row - 1, row + 2):
            if y < 0 or y >= len(lines):
                continue
            if lines[y][x] not in '.0123456789':
                # print('Row {}: {} is part'.format(row+1, num))
                return True
    # print('Row {}: {} is not part'.format(row+1, num))
    return False


def part1(lines) -> int:
    rsf = 0
    for row in range(len(lines)):
        nums = re.finditer(r'\d+', lines[row])
        for num in nums:
            if is_part(num.group(), num.start(), row, lines):
                rsf += int(num.group())
    return rsf


def add_gears(num, i, row, lines, gears):
    for x in range(i-1, i+len(num)+1):
        if x < 0 or x >= len(lines[0].strip()):
            continue
        for y in range(row - 1, row + 2):
            if y < 0 or y >= len(lines):
                continue
            if lines[y][x] == '*':
                if (y, x) in gears:
                    gears[y, x].append(int(num))
                else:
                    gears[y, x] = [int(num)]
    return False


def part2(lines) -> int:
    # gear coordinates: numbers
    gears = {}
    rsf = 0
    for row in range(len(lines)):
        nums = re.finditer(r'\d+', lines[row])
        for num in nums:
            add_gears(num.group(), num.start(), row, lines, gears)
    for gear in gears.items():
        nums = gear[1]
        if len(nums) == 2:
            rsf += nums[0] * nums[1]
    return rsf


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
