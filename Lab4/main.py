def write_to_file(ad_list: list[list[int]], n: int) -> None:
    with open("out.txt", "w") as f:
        for e in ad_list:
            f.write(f"{' '.join(map(str, e))}\n")
        f.write(str(n))


def read_from_file() -> tuple[int, list[list[int]]]:
    with open("in.txt") as f:
        n = int(f.readline())
        ad_matrix = [[int(num) for num in line.split()] for line in f]
    return n, ad_matrix


def prim(n: int, ad_matrix: list[list[int]]) -> tuple[list[list[int]], int]:
    w = 0
    F = {v for v in range(1, n)}
    near = [0 for _ in range(n)]
    d = [32767 for _ in range(n)]

    for v in F:
        near[v] = w
        d[v] = ad_matrix[v][w]

    T = set()
    while len(T) != n - 1:
        v = d.index(min(d))
        d[v] = 32767
        T |= {(v, near[v])}
        F -= {v}

        for u in F:
            if d[u] > ad_matrix[u][v]:
                d[u] = ad_matrix[u][v]
                near[u] = v

    ad_list = [[] for _ in range(n)]
    min_weight = 0
    for e in T:
        v, w = e[0], e[1]
        min_weight += ad_matrix[v][w]
        if w + 1 not in ad_list[v]:
            ad_list[v].append(w + 1)
        if v + 1 not in ad_list[w]:
            ad_list[w].append(v + 1)

    for v in ad_list:
        v.sort()
        v.append(0)

    return ad_list, min_weight


def main() -> None:
    write_to_file(*prim(*read_from_file()))


if __name__ == "__main__":
    main()
