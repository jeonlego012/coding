def dfs(graph, root):
    visit = []
    stack = []
    stack.append(root)

    while stack :
        node = stack.pop()
        if node not in visit :
            visit.append(node)
            stack.extend(graph[node])

    return visit

def solution(n, computers) :
    graph = {node : [] for node in range(n)}

    for i, computer in enumerate(computers) :
        for j, connection in enumerate(computer) :
            if i != j and connection == 1 :
                graph[i].append(j)
    
    possibleNetwork = map(sorted, [dfs(graph, node) for node in graph])
    return len(set(["".join(map(str, network)) for network in possibleNetwork]))