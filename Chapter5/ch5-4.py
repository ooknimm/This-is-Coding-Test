n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

import copy
graph2 = copy.deepcopy(graph)


def dfs(graph, x, y, count):
    if 0 > x or x >= n or 0 > y or y >= m:
        return count
    if graph[x][y] == 0:
        return count

    count += 1
    count = dfs(graph, x+1, y, count)
    count = dfs(graph, x, y+1, count)

    return count


def bfs(graph):
    from collections import deque
    queue = deque([[0,0]])
    count = 0
    move = [(0,1),(1,0),(0,-1),(-1,0)]
    while queue:
        x, y = queue.popleft()
        if graph[x][y] == 1:
            count += 1
            graph[x][y] = '*'
        for mv in move:
            x += mv[0]
            y += mv[1]
            if 0 <= x < n and 0 <= y < m:
                if graph[x][y] == 1:
                    queue.append([x,y])
    return count

print(dfs(graph,0,0,0))
print(bfs(graph2))
