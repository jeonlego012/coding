def check_range(y, x) :
    return y>=0 and y<n and x>=0 and x<m

def calculate(y, x) :
    max_sum = 0
    for tetromino in range(19) :
        tempY, tempX = y, x
        tetro_sum = paper[y][x]
        for move in range(3) :
            moveY, moveX = tempY + tetrominoY[tetromino][move], tempX + tetrominoX[tetromino][move]
            if check_range(moveY, moveX) :
                tempY, tempX = moveY, moveX
                tetro_sum += paper[tempY][tempX]
        max_sum = max(max_sum, tetro_sum)
    return max_sum


n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

tetrominoY = [[0,0,0], [0,1,0], [1,1,0], [1,0,1], [0,0,1],
                [1,1,1], [-1,0,0], [-1,0,0], [0,1,1], [1,1,0],
                [0,1,1], [1,0,0], [1,0,0], [1,0,1], [0,1,0],
                [0,1,0], [1,0,1], [1,1,-1], [0,-1,1]]
tetrominoX = [[1,1,1], [1,0,-1], [0,0,1], [0,1,0], [1,1,-1],
                [0,0,0], [0,1,1], [0,-1,-1], [1,0,0], [0,0,-1],
                [-1,0,0], [0,1,1], [0,-1,-1], [0,-1,0], [-1,0,-1],
                [1,0,1], [0,1,-1], [0,0,-1], [1,0,1]]

sum_list = []
for i in range(n) :
    for j in range(m) :
        sum_list.append(calculate(i, j))


print(max(sum_list))