count = 0

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
arr = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

for i in range(1, n+1):
    count = 0
    if ch[i] == 0:
        DFS(i)
        ch = [0] * (n + 1)
    arr[i] = count


for i in range(len(arr)):
    if arr[i] == max(arr):
        print(i, end=' ')