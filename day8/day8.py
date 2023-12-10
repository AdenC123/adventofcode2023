import math


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
    # either a node string or an int of its path length
    curr_nodes = []
    for line in lines[2:]:
        nodes[line[0:3]] = (line[7:10], line[12:15])
        if line[2] == 'A':
            curr_nodes.append(line[0:3])
    # do ins
    curr_ins = 0
    steps = 0
    num_done = 0
    while num_done != len(curr_nodes):
        # advance all curr_nodes
        for i in range(len(curr_nodes)):
            curr = curr_nodes[i]
            # check if cycled already
            if type(curr) is int:
                continue
            # do ins
            if ins[curr_ins] == 'L':
                curr_nodes[i] = nodes[curr][0]
            elif ins[curr_ins] == 'R':
                curr_nodes[i] = nodes[curr][1]
            curr = curr_nodes[i]
            if curr[2] == 'Z':
                # at end, replace with path len
                curr_nodes[i] = steps + 1
                num_done += 1
        steps += 1
        curr_ins = (curr_ins + 1) % len(ins)
    # print(curr_nodes)
    return math.lcm(*curr_nodes)


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
