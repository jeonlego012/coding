'''def solution(priorities, location) :
    printer = []
    front, rear = 0, len(priorities)-1
    for priority in range(len(priorities)) :
        while priorities :
            priorities.pop(front)
            front = (front+1) % len(priorities)
            rear = front + 1
'''
def other_solution(priorities, location): 
    count=0 
    while(len(priorities)!=0): 
        if location==0:
            if priorities[0]<max(priorities):
                priorities.append(priorities.pop(0))
                location=len(priorities)-1 
            else:
                return count+1 
        else: 
            if priorities[0]<max(priorities): 
                priorities.append(priorities.pop(0)) 
                location-=1 
            else: 
                priorities.pop(0) 
                location-=1 
                count+=1

def solution(priorities, location) :
    order = 0
    while priorities :
        if location == 0 :
            if priorities[0] < max(priorities) :
                priorities.append(priorities.pop(0))
                location = len(priorities)-1
            else :
                return order+1
        else :
            if priorities[0] < max(priorities) :
                priorities.append(priorities.pop(0))
                location -= 1
            else :
                priorities.pop(0)
                location -= 1
                order += 1



print(solution([2,1,3,2], 2))