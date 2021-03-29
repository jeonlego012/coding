def checkOneDifferent(word1, word2) :
    same = 0
    for i in range(len(word1)) :
        if word1[i] == word2[i] :
            same += 1
    if same == len(word1)-1 :
        return True
    else :
        return False

def solution(begin, target, words) :
    if target not in words :
        return 0
    
    graph = {}
    graph[0] = [begin]

    for i in range(1, len(words)) :
        possibleWords = []
        for j in range(len(graph[i-1])) :
            wordToCompare = graph[i-1][j]
            for k in range(len(words)) :
                if checkOneDifferent(words[k], wordToCompare) :
                    possibleWords.append(words[k])
        
        if target in possibleWords :
            return i
        graph[i] = possibleWords

