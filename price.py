def solution(prices) :
    increasingPeriod = [0 for i in range(len(prices))]
    for i in range(len(prices)-1) :
        for j in range(i, len(prices)-1) :
            if prices[i] <= prices[j] :
                increasingPeriod[i] += 1
            else :
                break
            
    return increasingPeriod

print(solution([1,2,3,2,3]))
