class Node:
    def __init__(self, data, next_node=None):
        self.data = data  # This will use the setter method for validation
        self.next_node = next_node  # This will use the setter method for validation

    @property
    def data(self):
        """Getter method for data"""
        return self._data

    @data.setter
    def data(self, value):
        """Setter method for data with validation"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Getter method for next_node"""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method for next_node with validation"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        """Prints the entire list"""
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """Inserts a new Node into the list in increasing order"""
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node


# Example usage:
# Creating a singly linked list and inserting nodes
sll = SinglyLinkedList()
sll.sorted_insert(10)
sll.sorted_insert(3)
sll.sorted_insert(5)
sll.sorted_insert(2)

# Printing the list
print(sll)