

# STRUCTURES


# GLOBALS


# MAIN
def part1(lines) -> int:
    ins = lines[0].strip()
    # map node: (left, right)
    nodes = {}
    for line in lines[2:]:
        nodes[line[0:3]] = (line[7:10], line[12:15])
    # do ins
    next_node = 'AAA'
    i = 0
    steps = 0
    while next_node != 'ZZZ':
        if ins[i] == 'L':
            next_node = nodes[next_node][0]
        elif ins[i] == 'R':
            next_node = nodes[next_node][1]
        steps += 1
        i = (i + 1) % len(ins)
    return steps


def part2(lines) -> int:
    ins = lines[0].strip()
    # map node: (left, right)
    nodes = {}
    curr_nodes = []
    for line in lines[2:]:
        nodes[line[0:3]] = (line[7:10], line[12:15])
        if line[2] == 'A':
            curr_nodes.append(line[0:3])
    # do ins
    i = 0
    steps = 0
    at_z = 0
    while at_z != len(curr_nodes):
        at_z = 0
        for j in range(len(curr_nodes)):
            if ins[i] == 'L':
                curr_nodes[j] = nodes[curr_nodes[j]][0]
            elif ins[i] == 'R':
                curr_nodes[j] = nodes[curr_nodes[j]][1]
            if curr_nodes[j][2] == 'Z':
                at_z += 1
        steps += 1
        if steps % 1000000 == 0:
            print(f'\r{steps}', end='')
        i = (i + 1) % len(ins)
    return steps


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
