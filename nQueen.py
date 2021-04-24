def is_available(current_candidate, current_col) :
    current_row = len(current_candidate)
    for row in range(current_row) :
        if current_candidate[row] == current_col or abs(current_candidate[row]-current_col) == current_row - row :
            return False
    return True


def dfs(current_row, current_candidate, queen) :
    if current_row == n:
        queen.append(current_candidate[:])
        return
    
    for candidate_col in range(n) :
        if is_available(current_candidate, candidate_col) :
            current_candidate.append(candidate_col)
            dfs(current_row+1, current_candidate, queen)
            current_candidate.pop()


n = int(input())
board = [[0]*n for _ in range(n)]

queen = []
dfs(0, [], queen)

print(len(queen))
#print(queen)