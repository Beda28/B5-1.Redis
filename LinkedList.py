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

    def remove(self, key):
        current = self.head

        while current:
            if current.key == key:
                if current.prev: current.prev.next = current.next
                else           : self.head         = current.next

                if current.next: current.next.prev = current.prev
                else           : self.tail         = current.prev

                self._size -= 1
                return True

            current = current.next
        return False

    def touch(self, key):
        self.remove(key)
        self.add_first(key)

    def pop_last(self):
        if self.tail is None: return None

        key = self.tail.key

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail      = self.tail.prev
            self.tail.next = None

        self._size -= 1
        return key

class Node:
    def __init__(self, key):
        self.key  = key
        self.prev = None
        self.next = None