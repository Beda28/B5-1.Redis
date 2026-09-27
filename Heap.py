class Heap:
    def __init__(self):
        self.data = []

    def push(self, expire_at, key):
        self.data.append((expire_at, key))
        self._heapify_up(len(self.data) - 1)

    def pop(self):
        if self.size() == 0: return None
        if self.size() == 1: return self.data.pop()

        root         = self.data[0]
        self.data[0] = self.data.pop()
        self._heapify_down(0)

        return root

    def peek(self):
        if self.size() == 0: return None
        return self.data[0]

    def size(self):
        return len(self.data)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.data[parent][0] <= self.data[index][0]: break

            self.data[parent], self.data[index] = self.data[index], self.data[parent]
            index = parent

    def _heapify_down(self, index):
        size = self.size()

        while True:
            left  = index * 2 + 1
            right = index * 2 + 2
            small = index

            if left < size and \
               self.data[left][0]  < self.data[small][0]: small = left

            if right < size and \
               self.data[right][0] < self.data[small][0]: small = right

            if small == index: break

            self.data[index], self.data[small] = self.data[small], self.data[index]
            index = small