def solution(n) :
    if n==1 :
        return '1'
    elif n==2 :
        return '2'
    elif n==3 :
        return '4'
    else :
        q, r = divmod(n-1, 3)
        return solution(q) + '124'[r]

print(solution(49))