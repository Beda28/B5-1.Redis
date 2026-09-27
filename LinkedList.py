class LinkedList:
    def __init__(self):
        self.head  = None
        self.tail  = None
        self._size = 0

    def add_first(self, key):
        node = Node(key)
        
        if self.head is None:
            self.head = node
            self.tail = node

        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        
        self._size += 1
        return node

    def remove_node(self, node):
        if node.prev : node.prev.next = node.next
        else         : self.head      = node.next

        if node.next : node.next.prev = node.prev
        else         : self.tail      = node.prev

        node.prev = None
        node.next = None

        self._size -= 1

    def move_to_front(self, node):
        if node == self.head: return

        if node.prev : node.prev.next = node.next
        if node.next : node.next.prev = node.prev
        else         : self.tail      = node.prev

        node.prev      = None
        node.next      = self.head
        self.head.prev = node
        self.head      = node

    def pop_last(self):
        if self.tail is None: return None

        node = self.tail

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail      = self.tail.prev
            self.tail.next = None

        node.prev = None
        node.next = None

        self._size -= 1
        return node

class Node:
    def __init__(self, key):
        self.key  = key
        self.prev = None
        self.next = None