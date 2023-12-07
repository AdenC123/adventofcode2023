# STRUCTURES


# GLOBALS
RANK = {
    'T': '10',
    'J': '11',
    'Q': '12',
    'K': '13',
    'A': '14'
}

RANK_P2 = {
    'T': '10',
    'J': '00',
    'Q': '12',
    'K': '13',
    'A': '14'
}


# MAIN
def get_type(hand: str) -> str:
    # 1 = high card, 2 = one pair, ..., 7 = five of a kind
    same_labels = []
    for card in hand:
        same_labels.append(hand.count(card))
    same_labels.sort(reverse=True)
    if same_labels[0] == 5:
        return '7'
    elif same_labels[0] == 4:
        return '6'
    elif same_labels == [3, 3, 3, 2, 2]:
        return '5'
    elif same_labels[0] == 3:
        return '4'
    elif same_labels == [2, 2, 2, 2, 1]:
        return '3'
    elif same_labels[0] == 2:
        return '2'
    else:
        return '1'


def card_key(line: str) -> int:
    # key = a bb cc dd ee ff
    # a is type, others are rank from first to last card
    hand = line.split()[0]
    key = [get_type(hand)]
    for card in hand:
        if card.isdigit():
            key.append('0' + card)
        else:
            key.append(RANK[card])
    key = int(''.join(key))
    # print(hand, key)
    return key


def part1(lines) -> int:
    lines.sort(key=card_key)
    rsf = 0
    for i in range(len(lines)):
        bid = int(lines[i].split()[1])
        rsf += (i + 1) * bid
    return rsf


def card_key_p2(line: str) -> int:
    # key = a bb cc dd ee ff
    # a is type, others are rank from first to last card
    hand = line.split()[0]
    if hand != 'JJJJJ':
        # replace all jokers with max card
        no_jokers = list(filter(lambda x: x != 'J', hand))
        max_card = max(set(no_jokers), key=no_jokers.count)
        wild_hand = hand.replace('J', max_card)
        key = [get_type(wild_hand)]
    else:
        key = ['7']
    for card in hand:
        if card.isdigit():
            key.append('0' + card)
        else:
            key.append(RANK_P2[card])
    key = int(''.join(key))
    # print(hand, key)
    return key


def part2(lines) -> int:
    lines.sort(key=card_key_p2)
    rsf = 0
    for i in range(len(lines)):
        bid = int(lines[i].split()[1])
        rsf += (i + 1) * bid
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
