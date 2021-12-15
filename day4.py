from typing import List, Tuple


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
    def __init__(self, rows: List[str]) -> None:
        self.rows = [list(map(int, r.split())) for r in rows]
        self.mask = [[0 for _ in r] for r in self.rows]

    def __repr__(self) -> str:
        return (
            "Rows: "
            + "\n".join(str(x) for x in self.rows)
            + "\nMask: "
            + "\n".join(str(x) for x in self.mask)
        )


def get_winning_board(input: str) -> Tuple[List[Board], int]:
    input = input.split("\n\n")
    numbers, boards = list(map(int, input[0].split(","))), input[1:]
    boards = [Board(b.split("\n")) for b in boards]
    for num in numbers:
        for board in boards:
            for idx, row in enumerate(board.rows):
                if num in row:
                    board.mask[idx][row.index(num)] = num
                    break
            row_wise = [a == b for (a, b) in zip(board.mask, board.rows)]
            col_wise = [
                [m[c] for m in board.mask] == [r[c] for r in board.rows]
                for c in range(len(board.rows[0]))
            ]
            if any(row_wise) or any(col_wise):
                return board, num
    return boards, num


def get_last_winning_board(input: str) -> Tuple[List[Board], int]:
    input = input.split("\n\n")
    numbers, boards = list(map(int, input[0].split(","))), input[1:]
    boards = [Board(b.split("\n")) for b in boards]
    winning_boards = []
    for num in numbers:
        for board_idx, board in enumerate(boards):
            if board_idx in winning_boards:
                continue
            for idx, row in enumerate(board.rows):
                if num in row:
                    board.mask[idx][row.index(num)] = num
                    break
            row_wise = [a == b for (a, b) in zip(board.mask, board.rows)]
            col_wise = [
                [m[c] for m in board.mask] == [r[c] for r in board.rows]
                for c in range(len(board.rows[0]))
            ]
            if any(row_wise) or any(col_wise):
                winning_boards.append(board_idx)
                if len(winning_boards) == len(boards):
                    return boards[board_idx], num
    return boards[winning_boards[-1]], num


def get_score(wb, wnum):
    rows, marked = wb.rows, wb.mask
    final = []
    for idx, row in enumerate(rows):
        for num in row:
            if num not in marked[idx]:
                final.append(num)
    return sum(final) * wnum  # reduce(lambda x, y: x * y, final, 1)


out = get_score(*get_winning_board(test_input))
assert out == 4512, out

with open("inputs/day4.txt", "r") as f:
    print(get_score(*get_winning_board(f.read())))

out = get_score(*get_last_winning_board(test_input))
assert out == 1924, out

with open("inputs/day4.txt", "r") as f:
    print(get_score(*get_last_winning_board(f.read())))
