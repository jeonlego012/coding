numOfExpressions = 0
def dfs(index, numbers, target) :
    global numOfExpressions
    if index < len(numbers) :
        numbers[index] *= 1
        dfs(index+1, numbers, target)

        numbers[index] *= -1
        dfs(index+1, numbers, target)

    elif sum(numbers) == target:
        numOfExpressions += 1
    
    return numOfExpressions


def solution(numbers, target) :
    global numOfExpressions
    numOfExpressions = dfs(0, numbers, target)
    return numOfExpressions