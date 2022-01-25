"""
It's a main file where we can test our Node and LinkedList functionality
"""

from LinkedList import LinkedList
from Node import Node

if __name__ == "__main__":

    my_list = LinkedList(Node(1))
    my_list.addNodeInList(Node(4), 1)
    my_list.addNodeInList(Node(34), 1)
    my_list.traverseList()
    print()
    my_list.addNodeInList(Node(5), 3)
    my_list.traverseList()
    print()
    print("delete node from list")
    my_list.deleteNodeFromList(5)
    my_list.traverseList()
    print()
    