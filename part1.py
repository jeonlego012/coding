def solution(L, x):
    index_list = []
    same = False
    for i in range(len(L)) :
        if L[i] == x :
            same = True
            index_list.append(i)
    if same == False :
        index_list.append(-1)
    return index_list

solution([64, 72, 83, 72, 54], 72)