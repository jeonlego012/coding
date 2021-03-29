from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def turn(d, c) :
    if c == 'L' :
        d = (d - 1) % 4
    else :
        d = (d + 1) % 4
    return d

def snakeGame() :
    direction = 0
    time = 1
    snakeY, snakeX = 0, 0
    snake = deque([[snakeY, snakeX]])
    board[snakeY][snakeX] = 2
    while True :
        snakeY, snakeX = snakeY + dy[direction], snakeX + dx[direction]
        if 0 <= snakeY < n and 0 <= snakeX < n and board[snakeY][snakeX] != 2 :
            if board[snakeY][snakeX] != 1 :
                removeY, removeX = snake.popleft()
                board[removeY][removeX] = 0
            board[snakeY][snakeX] = 2
            snake.append([snakeY, snakeX])
            if time in turnTime.keys() :
                direction = turn(direction, turnTime[time])
            time += 1
        else :
            return time


n = int(input())
k = int(input())
board = [[0]*n for i in range(n)]
for i in range(k) :
    appleY, appleX = map(int, input().split())
    board[appleY-1][appleX-1] = 1
l = int(input())
turnTime = {}
for i in range(l) :
    x, c = input().split()
    turnTime[int(x)] = c
print(snakeGame())