import itertools
def snail(n) :
    triangle = [[0]*i for i in range(1, n+1)]
    numOfSquare = sum(range(1, n+1))
    nextDirection = {'down' : 'right', 'right' : 'up', 'up' : 'down'}
    move = {'down' : (1, 0), 'right' : (0, 1), 'up' : (-1 , -1)}

    currentY, currentX, currentDirection = 0, 0, 'down'
    for number in range(1, numOfSquare+1) :
        triangle[currentY][currentX] = number
        print(triangle, currentDirection)
        nextY = currentY + move[currentDirection][0]
        nextX = currentX + move[currentDirection][1]
        if nextY < 0 or nextY >= n or nextX > nextY or triangle[nextY][nextX] != 0:
            currentDirection = nextDirection[currentDirection]
        currentY, currentX = currentY + move[currentDirection][0], currentX + move[currentDirection][1]
        
    return list(itertools.chain(*triangle))

print(snail(4))