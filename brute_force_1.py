def solution(answers):
    score = [0, 0, 0]
    max_score_soopoja = []
    soopoja_answer = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    for i in range(3) :
        for j in range(len(answers)) :
            if soopoja_answer[i][(j%len(soopoja_answer[i]))] == answers[j] :
                score[i]+=1

    for i in range(3):
        if score[i] == max(score) :
            max_score_soopoja.append(i+1)
    
    return max_score_soopoja

print(solution([1,3,2,4,2]))