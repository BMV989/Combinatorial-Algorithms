def dfs(x, graph, match, visited):
    for y in graph[x]:
        if not visited[y]:
            visited[y] = True
            if match[y] == -1 or dfs(match[y], graph, match, visited):
                match[y] = x
                return True
    return False


def find_maximum_matching(k, l, graph):
    match = [-1] * (l + 1)
    for x in range(1, k + 1):
        visited = [False] * (l + 1)
        if not dfs(x, graph, match, visited):
            return "N", x

    matching = []
    for y in range(1, l + 1):
        if match[y] != -1:
            matching.append((match[y], y))

    return "Y", matching


def main():
    with open("in.txt", "r") as f:
        k, l = map(int, f.readline().strip().split())
        graph = [[] for _ in range(k + 1)]

        for x in range(1, k + 1):
            edges = list(map(int, f.readline().strip().split()))
            for y in edges:
                if y == 0:
                    break
                graph[x].append(y)

    result, data = find_maximum_matching(k, l, graph)

    with open("out.txt", "w") as outfile:
        if result == "Y":
            outfile.write("Y\n")
            matching = [0] * (k + 1)
            for x, y in data:
                matching[x] = y
            outfile.write(' '.join(map(str, matching[1:])) + '\n')
        else:
            outfile.write("N\n")
            outfile.write(str(data) + '\n')


if __name__ == "__main__":
    main()
