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

    def _find_node(self, key):
        index   = self._hash(key)
        current = self.buckets[index]

        while current is not None:
            if current.key == key:
                return current
            current = current.next

        return None

    def put(self, key, value):
        index   = self._hash(key)
        current = self._find_node(key)

        if current is not None:
            current.value = value
            return

        new_node            = Node(key, value)
        new_node.next       = self.buckets[index]
        self.buckets[index] = new_node
        self.count         += 1

        if self.count / self.capacity > self.factor: 
            self._resize()

    def get(self, key):
        current = self._find_node(key)

        if current is not None: 
            return current.value        
        return None

    def remove(self, key):
        index    = self._hash(key)
        current  = self.buckets[index]
        previous = None

        while current is not None:
            if current.key == key:
                if previous is None:
                    self.buckets[index] = current.next
                else: 
                    previous.next = current.next
                
                self.count -= 1
                return True
            
            previous = current
            current  = current.next
        return False

    def contains(self, key):
        return self._find_node(key) is not None

    def keys(self):
        result = []

        for buckit in self.buckets:
            current = buckit

            while current is not None:
                result.append(current.key)
                current = current.next

        return result

    def size(self):
        return self.count

    def _resize(self):
        old_bucket = self.buckets

        self.capacity *= 2
        self.buckets   = [None] * self.capacity
        self.count     = 0

        for buckit in old_bucket:
            current = buckit

            while current is not None:
                self.put(current.key, current.value)
                current = current.next

class Node:
    def __init__(self, key, value):
        self.key   = key
        self.value = value
        self.next  = None