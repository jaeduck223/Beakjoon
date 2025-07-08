from collections import deque

a = [list(input()) for _ in range(12)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, color):
    q = deque([(x, y)])
    visited[x][y] = True
    group = [(x, y)]

    while q:
        cx, cy = q.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if not visited[nx][ny] and board[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    group.append((nx, ny))
    return group

def gravity():
    for col in range(6):
        stack = []
        for row in range(11, -1, -1):  # 아래에서 위로
            if board[row][col] != '.':
                stack.append(board[row][col])
        for row in range(11, -1, -1):
            board[row][col] = stack.pop(0) if stack else '.'

chain = 0
while True:
    visited = [[False]*6 for _ in range(12)]
    exploded = False

    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and not visited[i][j]:
                group = bfs(i, j, board[i][j])
                if len(group) >= 4:
                    exploded = True
                    for x, y in group:
                        board[x][y] = '.'

    if not exploded:
        break  
    gravity()
    chain += 1

print(chain)
