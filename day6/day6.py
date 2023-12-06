import re


# STRUCTURES


# GLOBALS


# MAIN
def do_race(hold, time) -> int:
    return hold * (time - hold)


def ways_to_win(time, record) -> int:
    rsf = 0
    found_low = False
    for hold in range(1, time):
        if do_race(hold, time) > record:
            found_low = True
            rsf += 1
        elif found_low:
            break
    return rsf


def part1(lines) -> int:
    # time: distance
    times = list(map(int, re.findall(r'\d+', lines[0])))
    records = list(map(int, re.findall(r'\d+', lines[1])))
    rsf = 1
    for i in range(len(times)):
        rsf *= ways_to_win(times[i], records[i])
    return rsf


def part2(lines) -> int:
    time = int(re.search(r'\d+', lines[0].replace(' ', '')).group())
    record = int(re.search(r'\d+', lines[1].replace(' ', '')).group())
    return ways_to_win(time, record)


def main():
    with open("test.txt") as f:
        lines = f.readlines()
        # print("Part 1 Test: " + str(part1(lines)))
        print("Part 2 Test: " + str(part2(lines)))
    with open("input.txt") as f:
        lines = f.readlines()
        # print("Part 1 Input: " + str(part1(lines)))
        print("Part 2 Input: " + str(part2(lines)))


if __name__ == '__main__':
    main()
