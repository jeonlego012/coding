from itertools import combinations

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def check_range(y, x):
    return y >= 0 and y < n and x >= 0 and x < m

def dfs(y, x):
    for move in range(4):
        moveY, moveX = y + dy[move], x + dx[move]
        if check_range(moveY, moveX) and after_laboratory[moveY][moveX] == 0:
            after_laboratory[moveY][moveX] = 2
            dfs(moveY, moveX)

n, m = map(int, input().split())
laboratory = [list(map(int, input().split())) for _ in range(n)]
wall = []
max_safe_num = 0

for i in range(n):
    for j in range(m):
        if laboratory[i][j] == 0:
            wall.append((i, j))
wall_combination = list(combinations(wall, 3))

# make wall
for make_wall in wall_combination:
    after_laboratory = [[0]*m for _ in range(n)]
    wall_num = 0
    safe_num = 0
    for i in range(n):
        for j in range(m):
            if wall_num < 3 and (i, j) == make_wall[wall_num]:
                after_laboratory[i][j] = 1
                wall_num += 1
            else:
                after_laboratory[i][j] = laboratory[i][j]
    # virus spread
    for y in range(n):
        for x in range(m):
            if after_laboratory[y][x] == 2:
                dfs(y, x)
    # count safe
    for i in range(n):
        for j in range(m):
            if after_laboratory[i][j] == 0:
                safe_num += 1
    max_safe_num = max(max_safe_num, safe_num)

print(max_safe_num)
