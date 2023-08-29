class Node:
    """
    This is the Node class.
    It defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.
        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional):
                The next node in the linked list. Defaults to None.
        Raises:
            TypeError:
                If data is not an integer.
            TypeError:
                If next_node is not None or a Node object.
        """
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    """
    This is the SinglyLinkedList class.
    It defines a singly linked list.
    """

    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted
        position in the list (increasing order).

        Args:
            value (int): The data to be stored in the new node.
        """
        new_node = Node(value)

        if self.head is None or self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not
            None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.
        """
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
