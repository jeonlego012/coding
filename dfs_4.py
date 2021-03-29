def solution(tickets) :
    tickets.sort(reverse=True)
    paths = {}
    for ticket1, ticket2 in tickets :
        if ticket1 in paths :
            paths[ticket1].append(ticket2)
        else :
            paths[ticket1] = [ticket2]
    
    start = ['ICN']
    visitPath = []
    while start :
        arrive = start[-1]
        if arrive not in paths or len(paths[arrive])==0 :
            visitPath.append(start.pop())
        else :
            start.append(paths[arrive].pop())

    visitPath.reverse()
    return visitPath