from collections import deque

n, m = map(int, input().split())
graph = [input().strip() for _ in range(n)]

# Find start (A) and end (B)
for y in range(n):
    for x in range(m):
        if graph[y][x] == 'A':
            ay, ax = y, x
        elif graph[y][x] == 'B':
            by, bx = y, x

# BFS setup
visited = [[False]*m for _ in range(n)]
parent = [[None]*m for _ in range(n)]
move_dir = [[None]*m for _ in range(n)]
dirs = [(-1,0,'U'), (1,0,'D'), (0,-1,'L'), (0,1,'R')]

q = deque()
q.append((ay, ax))
visited[ay][ax] = True

found = False
while q:
    y, x = q.popleft()
    if (y, x) == (by, bx):
        found = True
        break
    for dy, dx, move in dirs:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and graph[ny][nx] != '#':
            visited[ny][nx] = True
            parent[ny][nx] = (y, x)
            move_dir[ny][nx] = move
            q.append((ny, nx))

if not found:
    print("NO")
else:
    path = []
    y, x = by, bx
    while (y, x) != (ay, ax):
        path.append(move_dir[y][x])
        y, x = parent[y][x]
    path.reverse()
    print("YES")
    print(len(path))
    print(''.join(path))
