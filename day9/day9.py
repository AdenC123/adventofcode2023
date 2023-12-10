

# STRUCTURES


# GLOBALS


# MAIN
def get_next_val(history):
    # base case: all 0s
    his_set = set(history)
    if len(his_set) == 1 and list(his_set)[0] == 0:
        return 0
    # get diffs and return its next val
    diffs = []
    for i in range(1, len(history)):
        diffs.append(history[i] - history[i-1])
    return history[-1] + get_next_val(diffs)


def part1(lines) -> int:
    rsf = 0
    for line in lines:
        history = list(map(int, line.strip().split()))
        val = get_next_val(history)
        # print(val)
        rsf += val
    return rsf


def part2(lines) -> int:
    rsf = 0
    for line in lines:
        history = list(map(int, line.strip().split()))
        val = get_next_val(list(reversed(history)))
        # print(val)
        rsf += val
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
