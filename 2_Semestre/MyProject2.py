def DFS(g, s):
    explore = {s}
    visited = set()

    while len(explore) != 0:
        u = explore.pop()

        if u not in visited:
            visited.add(u)

            for v in g[u]:
                if v not in visited:
                    explore.add(v)

    return visited


def connectivityCheck(g, source, destination):
    visited = DFS(g, source)
    return destination in visited


G1 = {
    0: [1, 2, 3],
    1: [2],
    2: [4],
    3: [2],
    4: [5],
    5: [1]
}

G2 = {
    0: [1],
    1: [2],
    2: [3],
    3: []
}

G3 = {
    0: [1, 2],
    1: [2],
    2: [0],
    3: [4],
    4: []
}

print(connectivityCheck(G1, 0, 5))
print(connectivityCheck(G1, 2, 0))

print(connectivityCheck(G2, 0, 3))
print(connectivityCheck(G2, 3, 0))

print(connectivityCheck(G3, 0, 2))
print(connectivityCheck(G3, 0, 4))