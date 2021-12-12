test_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

from collections import Counter, defaultdict, deque
from functools import reduce


def count_common_bit_at_idx(bit_strings: list, bit_idx: int):
    bit_counter = Counter()
    for bit_string in bit_strings:
        bit_counter[bit_string[bit_idx]] += 1
    return (
        "1" if bit_counter["1"] > bit_counter["0"] else "0",
        "1" if bit_counter["1"] < bit_counter["0"] else "0",
    )


def count_common_bit(input: str):
    bit_strings = input.split("\n")
    gamma, epsilon = [], []
    n_cols = len(bit_strings[0])
    for bit_i in range(n_cols):
        bits = count_common_bit_at_idx(bit_strings, bit_i)
        gamma.append(bits[0]), epsilon.append(bits[1])
    return reduce(
        lambda x, y: x * y, [int("".join(gamma), 2), int("".join(epsilon), 2)]
    )


def get_rating(input: str, ox: bool = True):
    bit_strings = deque(input.split("\n"))
    bit_idx = 0
    while len(bit_strings) > 1:
        bit_counter = defaultdict(list)
        for bit_string in bit_strings:
            bit_counter[bit_string[bit_idx]].append(bit_string)
        if ox:
            if len(bit_counter["1"]) >= len(bit_counter["0"]):
                bit_strings = bit_counter["1"]
            else:
                bit_strings = bit_counter["0"]
        else:
            if len(bit_counter["0"]) <= len(bit_counter["1"]):
                bit_strings = bit_counter["0"]
            else:
                bit_strings = bit_counter["1"]
        bit_idx += 1
    return int(bit_strings[0], 2)


assert count_common_bit(test_input) == 198
assert get_rating(test_input, True) * get_rating(test_input, False) == 230

with open("inputs/day3.txt", "r") as f:
    input = f.read()
    print(count_common_bit(input))
    print(get_rating(input, True) * get_rating(input, False))
