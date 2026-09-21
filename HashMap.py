class HashMap:
    def __init__(self, capacity = 8):
        self.capacity = capacity
        self.buckets  = [None] * capacity
        self.count    = 0
        self.factor   = 0.75

    def _hash(self, key):
        hash_value = 0
        for char in key:
            hash_value = hash_value * 31 + ord(char)
        return hash_value % self.capacity

    def put(self, key, value):
        index   = self._hash(key)
        current = self.buckets[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_node            = Node(key, value)
        new_node.next       = self.buckets[index]
        self.buckets[index] = new_node
        self.count         += 1

        if self.count / self.capacity > self.factor: 
            pass

    def get(self, key):
        pass

class Node:
    def __init__(self, key, value):
        self.key   = key
        self.value = value
        self.next  = None