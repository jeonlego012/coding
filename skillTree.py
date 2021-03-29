def solution(skills, skillTrees) :
    numOfPossibleSkillTrees = 0
    
    for skillTree in skillTrees :
        possible = True
        remain = ""
        for skill in skillTree :
            
            if skill in skills :
                remain += skill
                
        print("final : " + remain)
        for i in range(len(remain)) :
            print(skills[i] + ", " + remain[i])
            if skills[i] != remain[i] :
                possible = False
                break
        if possible :
            numOfPossibleSkillTrees += 1
    return numOfPossibleSkillTrees


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))