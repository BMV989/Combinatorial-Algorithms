from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Delta:
    x: int
    y: int


@dataclass
class ChessFigure:
    char: int
    number: int

    def is_on_board(self) -> bool:
        return (1 <= self.number <= 8
                and 97 <= self.char <= 104)

    def get_position(self) -> str:
        return f"{chr(self.char)}{self.number}"

    def is_in_danger(self, pawn: ChessFigure) -> bool:
        pawn_left_attack = ChessFigure(pawn.char - 1, pawn.number - 1)
        pawn_right_attack = ChessFigure(pawn.char + 1, pawn.number - 1)
        return self == pawn_left_attack or self == pawn_right_attack


def make_chess_board() -> list[list[bool]]:
    return [[False for _ in range(9)] for _ in range(9)]


def read_from_file() -> tuple[ChessFigure, ChessFigure]:
    with open("in.txt") as f:
        lines = f.readlines()
        return (ChessFigure(ord(lines[0][0]), int(lines[0][1])),
                ChessFigure(ord(lines[1][0]), int(lines[1][1])))


def write_to_file(text: str) -> None:
    with open("out.txt", "w") as f:
        f.write(text)


def dfs(visited: list[list[bool]],
        knight: ChessFigure, pawn: ChessFigure) -> bool:
    dts = [Delta(-1, 2), Delta(1, 2), Delta(2, 1), Delta(2, -1),
           Delta(1, -2), Delta(-1, -2), Delta(-2, -1), Delta(-2, 1)]
    if (not knight.is_on_board() or knight.is_in_danger(pawn)
            or visited[knight.char - 96][knight.number]):
        return False
    visited[knight.char - 96][knight.number] = True
    if knight == pawn:
        dfs.result = pawn.get_position()
        return True
    for delta in dts:
        new_pos = ChessFigure(knight.char + delta.x,
                              knight.number + delta.y)
        if dfs(visited, new_pos, pawn):
            dfs.result = f"{knight.get_position()}\n{dfs.result}"
            return True
    return False


def main() -> None:
    dfs.result = ""
    knight, pawn = read_from_file()
    dfs(make_chess_board(), knight, pawn)
    write_to_file(dfs.result)


if __name__ == "__main__":
    main()
