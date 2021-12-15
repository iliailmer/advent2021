test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


class Board:
    def __init__(self, rows: list) -> None:
        self.rows = [list(map(int, r.split())) for r in rows]
        self.mask = [[] for _ in rows]

    def __repr__(self) -> str:
        return (
            "Rows: "
            + "\n".join(str(x) for x in self.rows)
            + "\nMask: "
            + "\n".join(str(x) for x in self.mask)
        )


def get_winning_board(input: str):
    input = input.split("\n\n")
    numbers, boards = list(map(int, input[0].split(","))), input[1:]
    boards = [Board(b.split("\n")) for b in boards]
    for num in numbers:
        for board in boards:
            for idx, row in enumerate(board.rows):
                if num in row:
                    board.mask[idx].append(int(num))
                    break
            if any(len(mask) == len(board.rows[0]) for mask in board.mask):
                return board, num
    return boards


def get_score(input: str):
    wb, wnum = get_winning_board(input)
    rows, marked = wb.rows, wb.mask
    final = []
    for idx, row in enumerate(rows):
        for num in row:
            if not num in marked[idx]:
                final.append(num)
    return sum(final) * wnum  # reduce(lambda x, y: x * y, final, 1)


out = get_score(test_input)
assert out == 4512, out

with open("inputs/day4.txt", "r") as f:
    print(get_score(f.read()))
