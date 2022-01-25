"""
This class is responsible to create linked list with the help of Node class
and handle all the Linked List's operations
"""

from Node import Node

class LinkedList:
    def __init__(self, node = None) -> None:
        self.head = node

    def traverseList(self):
        self.head.print()
    
    def addNodeInList(self, node, pos):
        """
        This will add node in list at any position
        """

        if pos < 1 or pos > Node.length:
            return None
        elif pos == 1:
            node.next = self.head
            self.head  = node
        else:
            current_cursor = self.head
            previous_cursor = None
            for _ in range(pos-1):
                previos_cursor = current_cursor
                current_cursor = current_cursor.next
            node.next = current_cursor
            previos_cursor.next = node
    
    def deleteNodeFromList(self, pos):
        """
        This will delete node from the list 
        """
        if pos < 1 or pos > Node.length:
            return None
        elif pos == 1:
            self.head = self.head.next
        else:
            current_cursor = self.head
            previous_cursor = self.head
            for _ in range(pos-1):
                previous_cursor = current_cursor
                current_cursor = current_cursor.next
                
            previous_cursor.next = current_cursor.next
            current_cursor.setNext(None)
        Node.length -= 1