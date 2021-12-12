from itertools import islice

test_input = """
199
200
208
210
200
207
240
269
260
263
"""


def count_increases(input: str, window: int = 1):
    lines = list(map(int, filter(lambda x: x != "", input.split("\n"))))
    cur = prev = 0
    counter = -1
    for i in range(len(lines) - window + 1):
        cur = sum(lines[i : i + window])
        if cur > prev:
            counter += 1
        prev = cur
    return counter


assert count_increases(test_input) == 7


assert count_increases(test_input, 3) == 5

with open("inputs/day1.txt", "r") as f:
    input = f.read()
    print(count_increases(input))
    print(count_increases(input, 3))
