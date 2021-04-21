straight = [(-1,0), (0,1), (1,0), (0,-1)]
back = [(1,0), (0,-1), (-1,0), (0,1)]
left = [(0,-1), (-1,0), (0,1), (1,0)]

only_rotate = 0
num_clean = 0

def clean(y, x) :
    global num_clean
    room[y][x] = 2
    num_clean += 1
    return room

def go_straight(y, x, direction) :
    y, x = y + straight[direction][0], x + straight[direction][1]
    return y,x

def go_back(y, x, direction) :
    y, x= y + back[direction][0], x + back[direction][1]
    return y, x

def turn_left(direction) :
    direction = (direction+3) % 4
    return direction

n, m = map(int, input().split())
y, x, direction = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

clean(y, x)

while True :
    if only_rotate == 4 :
        if room[y+back[direction][0]][x+back[direction][1]] == 1 :
            break
        else :
            y, x = go_back(y, x, direction)
            only_rotate = 0

    elif room[y+left[direction][0]][x+left[direction][1]] == 0 :
        direction = turn_left(direction)
        y, x = go_straight(y, x, direction)
        room = clean(y, x)
        only_rotate = 0
    
    elif room[y+left[direction][0]][x+left[direction][1]] != 0 :
        direction = turn_left(direction)
        only_rotate += 1

print(num_clean)