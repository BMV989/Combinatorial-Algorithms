def write_to_file(data: str) -> None:
    with open("out.txt", "w") as f:
        f.write(data)


def read_from_file() -> tuple[list[list[int]], int, int]:
    with open("in.txt") as f:
        n = int(f.readline())
        lines = f.readlines()
        weight_matrix = [[int(e) for e in line.split()] for line in lines[:n]]
        return weight_matrix, int(lines[-2]), int(lines[-1])


def max_pathfinder(weight_matrix: list[list[int]], start: int, end: int) -> tuple[list[int], int] | None:
    start -= 1
    end -= 1
    vertices = set(range(len(weight_matrix)))

    def get_successors(s):
        return set([
            e for e in vertices
            if weight_matrix[s][e] != -32768
        ])

    def get_ancestors(e):
        return set([s for s in vertices
                    if weight_matrix[s][e] != -32768])

    def topological_sort():
        degrees = dict([
            (v, len(get_successors(v)))
            for v in vertices
        ])
        stack = [v for v in vertices if degrees[v] == 0]
        ans = dict()
        for i in range(len(vertices)):
            v = stack.pop()
            ans[v] = len(vertices) - 1 - i
            for w in get_ancestors(v):
                degrees[w] -= 1
                if degrees[w] == 0: stack.append(w)
        return ans

    def pathfinder():
        ids = topological_sort()

        new_vertices = dict([
            (i, v) for (v, i) in ids.items()
        ])

        distances = dict([
            (v, weight_matrix[start][v])
            for v in vertices])

        parents = dict([
            (v, start) for v in vertices
            if weight_matrix[start][v] != -32768])

        parents[start] = start

        for i in range(ids[start] + 1, len(vertices)):
            v = new_vertices[i]
            for w in get_ancestors(v):
                through_w = distances[w] + weight_matrix[w][v]
                if through_w > distances[v]:
                    distances[v] = through_w
                    parents[v] = w

        if distances[end] == -32768:
            return None

        path = []

        cur = end

        while parents[cur] != cur:
            path.append(cur + 1)
            cur = parents[cur]

        path.append(start + 1)
        return path[::-1], distances[end]

    return pathfinder()


def main() -> None:
    ans = max_pathfinder(*read_from_file())
    if ans:
        write_to_file(f"Y\n{" ".join(map(str, ans[0]))}\n{ans[1]}")
    else:
        write_to_file("N")


if __name__ == "__main__":
    main()
