#!/usr/bin/python3


"""A class representing a node of a singly linked list."""


class Node:
    """
    A class representing a node of a singly linked list.

    Attributes:
        __data (int): The data value of the node (private).
        __next_node (Node): The reference to the next node (private).
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a Node instance with data and next_node.

        Args:
            data (int): The data value of the node.
            next_node (Node, optional): The reference to the next node.
            Defaults to None.

        Raises:
            TypeError: If data is not an integer or if next_node is not
            None or a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method to retrieve the data attribute.

        Returns:
            int: The data value of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to set the data attribute.

        Args:
            value (int): The data value of the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method to retrieve the next_node attribute.

        Returns:
            Node: The reference to the next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next_node attribute.

        Args:
            value (Node): The reference to the next node.

        Raises:
            TypeError: If value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""A class representing a singly linked list."""


class SinglyLinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head: The head of the linked list.
    """
    def __init__(self):
        """
        Initializes an empty SinglyLinkedList.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list
        (increasing order).

        Args:
            value (int): The value to be inserted into the list.
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and
            current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        String representation of the SinglyLinkedList.

        Returns:
            str: The string representation of the linked list.
        """
        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
