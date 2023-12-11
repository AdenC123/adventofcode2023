

# STRUCTURES


# GLOBALS
# maps pipe to the coordinates it connects relative to pipe at (0, 0)
ADJ = {
    '|': ((0, -1), (0, 1)),
    '-': ((-1, 0), (1, 0)),
    'L': ((0, -1), (1, 0)),
    'J': ((0, -1), (-1, 0)),
    '7': ((-1, 0), (0, 1)),
    'F': ((1, 0), (0, 1)),
}


# MAIN
# def get_all_adj(point, graph):
#     ret = []
#     for p in (point[0]+1, point[1]), (point[0]-1, point[1]), (point[0], point[1]+1), (point[0], point[1]-1):
#         if 0 <= p[0] < len(graph[0]) and 0 <= p[1] < len(graph):
#             ret.append(p)
#     return tuple(ret)


def get_next_point(point, prev, graph):
    char = graph[point[1]][point[0]]
    for p in ADJ[char]:
        next_p = tuple([sum(x) for x in zip(point, p)])
        if next_p != prev:
            return next_p


def part1(graph, p1, p2) -> int:
    start = (0, 0)
    for i, row in enumerate(graph):
        if 'S' in row:
            start = (row.index('S'), i)
    prev_p1, prev_p2 = start, start
    steps = 1
    while p1 != p2:
        prev_p1, p1 = p1, get_next_point(p1, prev_p1, graph)
        prev_p2, p2 = p2, get_next_point(p2, prev_p2, graph)
        steps += 1
    return steps


def is_inside(col, row, path, graph):
    if (col, row) in path:
        return False
    cross = 0
    for x in range(col, len(graph[0])):
        if graph[row][x] in '|JL' and (x, row) in path:
            cross += 1
    return cross % 2 == 1


def part2(graph, p1, p2) -> int:
    # remove newlines from graph
    for i in range(len(graph)):
        graph[i] = graph[i].strip()
    # store path as set of points
    start = (0, 0)
    for i, row in enumerate(graph):
        if 'S' in row:
            start = (row.index('S'), i)
            break
    prev_p1, prev_p2 = start, start
    path = {start}
    while p1 != p2:
        path.add(p1)
        path.add(p2)
        prev_p1, p1 = p1, get_next_point(p1, prev_p1, graph)
        prev_p2, p2 = p2, get_next_point(p2, prev_p2, graph)
    path.add(p1)
    # shoot ray right from each point, count times it crosses path
    inside = 0
    for x in range(len(graph[0])):
        for y in range(len(graph)):
            if is_inside(x, y, path, graph):
                # graph[y] = graph[y][:x] + 'I' + graph[y][x+1:]
                inside += 1
    # for row in graph:
    #     print(row)
    return inside


def main():
    with open("test.txt") as f:
        lines = f.readlines()
        # print("Part 1 Test: " + str(part1(lines, (1, 2), (0, 3))))
        print("Part 2 Test: " + str(part2(lines, (2, 1), (1, 2))))
    with open("input.txt") as f:
        lines = f.readlines()
        # print("Part 1 Input: " + str(part1(lines, (23, 76), (24, 77))))
        print("Part 2 Input: " + str(part2(lines, (23, 76), (24, 77))))


if __name__ == '__main__':
    main()
