import re


# STRUCTURES


# GLOBALS


# MAIN
def part1(lines) -> int:
    rsf = 0
    for line in lines:
        m = matches(line)
        if m > 0:
            rsf += 2 ** (m - 1)
    return rsf


def matches(line):
    all_nums = re.findall(r'\d+|\|', line)[1:]
    winning_nums = []
    i = 0
    while all_nums[i] != '|':
        winning_nums.append(all_nums[i])
        i += 1
    my_nums = all_nums[i + 1:]
    rsf = 0
    for num in my_nums:
        if num in winning_nums:
            rsf += 1
    return rsf


def part2(lines) -> int:
    cards = [1 for _ in range(len(lines))]
    for i in range(len(cards)):
        m = matches(lines[i])
        # print(cards)
        for j in range(1, m+1):
            cards[i+j] += cards[i]
    return sum(cards)


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
