dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
roll = [[0, 1, 4, 3], [0, 3, 4, 1], [0, 2, 4, 5], [0, 5, 4, 2]]

def go(direction) :
    temp = [0]*6
    for i in range(4) :
        temp[i] = dice[roll[direction][i]]
    for i in range(4) :
        dice[roll[direction][(i+1)%4]] = temp[i]

def check_range(y, x) :
    return y>=0 and y<n and x>=0 and x<m

n, m, y, x, k = map(int, input().split())
map_ = [list(map(int, input().split())) for _ in range(n)]
dice = [0]*6

d = list(map(int, input().split()))
for i in range(k) :
    nextY, nextX = y + dy[d[i]-1], x + dx[d[i]-1]
    if check_range(nextY, nextX) == False : continue
    y, x = nextY, nextX
    go(d[i]-1)
    if map_[y][x] == 0 :
        map_[y][x] = dice[4]
    else :
        dice[4] = map_[y][x]
        map_[y][x] = 0
    print(dice[0])
