count = 0
def DFS(v):
    global count
    ch[v] = 1
    for nv in graph[v]:
        if ch[nv] == 0:
            DFS(nv)
            count += 1


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
ch = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

DFS(1)

print(count)