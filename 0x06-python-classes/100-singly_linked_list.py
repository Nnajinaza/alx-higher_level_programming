#!/usr/bin/python3
"""Defines a class Square"""


class Node:
    """Initialize th square class"""
    def __init__(self, data, next_node=None):
        """
        Args:
            data (int): The value of the size of the square
            next_node (Node): value of the node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """To retrieve the size"""
        return self.__data

    @data.setter
    def data(self, value):
        """To set the value of size"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """To retrieve the positon"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """To set values of  position"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Initialize th square class"""
    def __init__(self):
        """
        Args:
            head (Node): head node
        """
        self.__head = None

    def sorted_insert(self, value):
        """Function to sort the list"""
        new_node = Node(value, None)
        temp = self.__head
        if not self.__head:
            self.__head = new_node
            return
        if temp.data > value:
            new_node.next_node = temp
            self.__head = new_node
            return
        while temp.next_node is not None:
            if temp.next_node.data > value:
                break
            temp = temp.next_node
        new_node.next_node = temp.next_node
        temp.next_node = new_node
        return

    def __str__(self):
        """define special __str__ method for printing the list values
        when print(self) is called """
        list_values = ''
        temp = self.__head
        while temp is not None:
            list_values += str(temp.data)
            if temp.next_node is not None:
                list_values += '\n'
            temp = temp.next_node
        return list_values
