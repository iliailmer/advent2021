test_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def get_product(input: str):
    hor, depth, aim = 0, 0, 0  # hor=horizontal, depth = vertical
    for line in input.split("\n"):
        com, dig = line.split(" ")
        if com == "forward":
            hor += int(dig)
            depth += int(dig) * aim
        if com == "up":
            aim -= int(dig)
        if com == "down":
            aim += int(dig)
    return hor * depth


# assert get_product(test_input) == 150
assert get_product(test_input) == 900
with open("inputs/day2.txt", "r") as f:
    input = f.read()
    print(get_product(input))
