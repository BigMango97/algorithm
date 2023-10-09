from collections import deque

graph = {
    'A':['B','D','E'],
    'B':['A','C','D'],
    'C':['B'],
    'D':['A','B'],
    'E':['A']
}
#1. BFS -> 너비 우선 탐색(큐)

def bfs(graph, start_v):
    visited = [start_v]
    queue = deque(start_v)
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited
print(bfs(graph,'A')) #['A', 'B', 'D', 'E', 'C']

#2. DFS -> 깊이 우선 탐색(재귀)

visited =[]
def dfs(cur_v):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            dfs(v)
dfs('A')
print(visited) #['A', 'B', 'C', 'D', 'E']