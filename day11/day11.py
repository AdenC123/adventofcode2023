import itertools


# STRUCTURES


# GLOBALS


# MAIN
def expand_rows(i, galaxies):
    pass


def find_dist(gals):
    return abs(gals[0][0] - gals[1][0]) + abs(gals[0][1] - gals[1][1])


def part1(lines) -> int:
    # expand rows
    row = 0
    while row < len(lines):
        lines[row] = lines[row].strip()
        if '#' not in lines[row]:
            lines.insert(row, '.' * len(lines[0]))
            row += 1
        row += 1
    # expand cols
    col = 0
    while col < len(lines[0]):
        if '#' not in [lines[row][col] for row in range(len(lines))]:
            for i, row in enumerate(lines):
                lines[i] = row[:col] + '.' + row[col:]
            col += 1
        col += 1
    # find galaxies
    galaxies = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '#':
                galaxies.append((j, i))
    # sum all distances
    return sum(map(find_dist, itertools.combinations(galaxies, 2)))


def part2(lines) -> int:
    return 0


def main():
    with open("test.txt") as f:
        lines = f.readlines()
        print("Part 1 Test: " + str(part1(lines)))
        # print("Part 2 Test: " + str(part2(lines)))
    with open("input.txt") as f:
        lines = f.readlines()
        print("Part 1 Input: " + str(part1(lines)))
        # print("Part 2 Input: " + str(part2(lines)))


if __name__ == '__main__':
    main()
