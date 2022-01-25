"""
This Class defines the behaviour of particular Node
responsible to maintain the count of object as well
"""

class Node:
    length = 0

    def __init__(self,  data = None, next = None) -> None:
        self.data = data
        self.next = next
        Node.length += 1  
    
    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next
    
    def getNext(self):
        return self.next

    def getData(self):
        return self.data
    
    def hasNext(self):
        return self.next != None
    
    def print(self):
        print("->", self.data, end="")
        if self.hasNext():
            self.next.print()

