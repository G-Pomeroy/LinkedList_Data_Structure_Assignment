from node import Node


# Initialize the LinkedList
class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        self.size = 0

# Checks LinkedList to ensure that there are no values
        if values is not None:
            for value in values:
                self.append(value)

# Adds new node to the end of the LinkedList
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

# Adds new node to the beginning of the LinkedList
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        self.size += 1

# Returns total number of nodes currently in the LinkedList
    def size(self):
        return self.size

# Returns the current node at the beginning of the LinkedList
    def head(self):
        return self.head

# Returns the current node at the end of the LinkedList
    def tail(self):
        return self.tail

# Returns the node at the given index
    def index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head
        for x in range(index):
            current = current.next
        return current

# Removes the last item in the LinkedList
    def pop(self):
        if not self.head:
            raise Exception("List is empty")
        current = self.head
        previous = None
        while current.next:
            previous = current
            current = current.next
        if previous:
            previous.next = None
            self.tail = previous
        else:
            self.head = None
            self.tail = None
        self.size -= 1
        return current.value

# Checks the LinkedList if it contains given value (Bool)
    def contains(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

# Returns the node of the given value. Returns None if not found.
    def find(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return None

# Prints every value currently in LinkedList
    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
