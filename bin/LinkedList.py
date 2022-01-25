"""
This class is responsible to create linked list with the help of Node class
and handle all the Linked List's operations
"""

import Node

class LinkedList():
    def __init__(self, node = None) -> None:
        self.head = node

    def traverseList(self):
        self.head.print()