class Node:
    def __init__(self, item) :
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self) :
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, position) :
        if position < 1 or position > self.nodeCount :
            return None
        i = 1
        current = self.head
        while i<position :
            current = current.next
            i += 1
        return current

    def traverse(self) :
        linkedList = []
        current = self.head
        while current != None :
            linkedList.append(current.data)
            current = current.next

        return linkedList