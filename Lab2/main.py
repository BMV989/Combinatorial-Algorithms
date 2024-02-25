from collections import deque


def read_from_file() -> tuple[int, list[list[int]]]:
    with open("in.txt") as f:
        n = int(f.readline())
        ad_matrix = [[int(num) for num in line.split()] for line in f]
    return n, ad_matrix


def write_to_file(text: str) -> None:
    with open("out.txt", "w") as f:
        f.write(text)


def bfs(vertex_count: int, ad_matrix: list[list[int]]) -> list[int] | None:
    def find_cycle(start: int, end: int) -> list[int]:
        cycle = []
        while start != end:
            cycle.append(end + 1)
            cycle.append(start + 1)
            start, end = parent[start], parent[end]
        cycle.append(start + 1)
        return cycle[::-1]

    def process_component() -> list[int] | None:
        while queue:
            e = queue.popleft()
            for i in range(vertex_count):
                if ad_matrix[e][i]:
                    if parent[i] == -1:
                        queue.append(i)
                        parent[i] = e
                    elif parent[e] != i:
                        return find_cycle(e, i)
        if -1 in parent:
            queue.append(parent.index(-1))
            parent[parent.index(-1)] = -2
            return process_component()
        return None

    parent = [-1] * vertex_count
    parent[0] = -2
    queue = deque([0])
    return process_component()


def main() -> None:
    n, ad_matrix = read_from_file()
    cycle = bfs(n, ad_matrix)
    if not cycle:
        write_to_file("A")
    else:
        write_to_file(f"N\n{" ".join(map(str, cycle))}")


if __name__ == "__main__":
    main()
