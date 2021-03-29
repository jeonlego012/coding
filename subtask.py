'''
n, m, k = map(int, input().split())
k = k % 4
array = [[int(x) for x in input().split()] for y in range()
for y in range(n):
    for x in range(m):
        array[y][x] = int(input().split())
'''
'''
n = int(input())
path = input()

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

ghostY, ghostX = 0, 0

for i in range(n) :
    ghostY = ghostY + dy[int(path[i])]
    ghostX = ghostX + dx[int(path[i])]

print(ghostY, ghostX)
'''
'''
import string
which = input()
print(string.ascii_lowercase.index(which))
'''

'''
def check(i, j) :
    y, x = i, j
    matrix[i][j] = 0
    for k in range(4) :
        y = i + dy[k]
        x = j + dx[k]
        if y>=0 and y<n and x>=0 and x<m and matrix[y][x] == 1 :
            check(y, x)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
ghostTown = 0
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n) :
    for j in range(m) :
        if matrix[i][j] == 1 :
            ghostTown += 1
            check(i, j)

print(ghostTown)
'''

'''
n, m, k = map(int, input().split())
spiral = [[0]*m for _ in range(n)]


directionY = [0, 1, 0, -1]
directionX = [1, 0, -1, 0]

def change_direction(y, x) :
    return ((x==m-1) and (y==n-1)) or x==m-1 or ((x==0) and (y==n-1))

def rotate_clock() :

y, x, ghost = 0, 0, 1

for move in range(n*m) :
    spiral[y][x] = ghost

    if change_direction :
        y += 
'''

'''
n, m, k = map(int, input().split())
spiral = [[0]*m for _ in range(n)]

directionY = [0, 1, 0, -1]
directionX = [1, 0, -1, 0]

def rotate() :
  

y, x, ghost = 0, 0, 1
for move in range(n*m) :
  spiral[y][x] = ghost
  if spiral[y][x+1] 
  '''

go = [-1, 1]

n, x, d, t = map(int, input().split())

for time in range(t) :
    nextX = x + go[d]
    if nextX == -1 :
        d = 1
        x += 1
    elif nextX == n :
        d = 0
        x -= 1
    else :
        x = nextX

print(x)

