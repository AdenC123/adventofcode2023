import re

# STRUCTURES


# GLOBALS
MAX = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


# HELPERS


# MAIN
def part1(lines) -> int:
    rsf = 0
    for line in lines:
        possible = True
        id = int(re.search(r'\d+', line).group())
        games = line.split(':')[1].strip()
        for game in re.split(r'[,;]', games):
            game = game.strip()
            num = int(re.search(r'\d+', game).group())
            color = game.split(' ')[1]
            # print(id, num, color)
            if num > MAX[color]:
                possible = False
                break
        if possible:
            rsf += id
    return rsf


def part2(lines) -> int:
    rsf = 0
    for line in lines:
        mins = {"red": 0, "green": 0, "blue": 0}
        games = line.split(':')[1].strip()
        for game in re.split(r'[,;]', games):
            game = game.strip()
            num = int(re.search(r'\d+', game).group())
            color = game.split(' ')[1]
            mins[color] = max(mins[color], num)
        rsf += mins["red"] * mins["green"] * mins["blue"]
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
