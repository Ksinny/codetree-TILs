count = 0
max = 0


def DFS(v):
    global count
    ch[v] += 1
    for nv in graph[v]:
        if ch[nv] == 0:
            count += 1
            DFS(nv)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
ch = [0] * (n + 1)
arr = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

for i in range(1, n+1):
    if ch[i] == 0:
        DFS(i)
        if max == count:
            arr.append(i)
        elif max < count:
            arr.clear()
            arr.append(i)
            max = count
    count = 0
    ch = [0] * (n + 1)

print(*arr)