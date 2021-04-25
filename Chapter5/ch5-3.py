n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append((list(map(int, input()))))

from copy import deepcopy
graph2 = deepcopy(graph)


from collections import deque
def ice_count(graph):
    def bfs(graph, row, col):
        _map = [(0,1), (1,0), (0,-1), (-1,0)]
        q = deque([[row, col]])
        while q:
            row, col = q.popleft()
            graph[row][col] = 1
            for m in _map:
                t_row = row + m[0]
                t_col = col + m[1]
                if 0 <= t_row < len(graph) and 0 <= t_col < len(graph[t_row]):
                    if graph[t_row][t_col] == 0:
                        q.append([t_row, t_col])
                        graph[t_row][t_col] = 1

    count = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 0:
                bfs(graph, i, j)
                count += 1
    return count


def ice_count2(graph):
    def dfs(row, col):
        if 0 > row or row >= n or 0 > col or col >= m:
            return
        
        if graph[row][col] == 0:
            graph[row][col] = 1
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

    count = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 0:
                dfs(i,j)
                count+= 1
    return count 


print(ice_count(graph))
print(ice_count2(graph2))
