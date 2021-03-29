import math
def solution(progresses, speeds) :
    numOfFunctionPerDistribution = []
    daysToDevelop = [math.ceil((100-progress)/speed) for progress, speed in zip(progresses, speeds)]
    first = 0
    for i in range(len(daysToDevelop)) :
        if daysToDevelop[first] < daysToDevelop[i] :
            numOfFunctionPerDistribution.append(i-first)
            first = i
    numOfFunctionPerDistribution.append(len(daysToDevelop)-first)
    
    return numOfFunctionPerDistribution

    

print(solution([93, 30, 55], [1, 30, 5]))