from HashMap    import HashMap
from LinkedList import LinkedList

class RedisKeyValue:
    def __init__(self):
        self.Hash = HashMap()
        self.Link = LinkedList()

        self.max_memory = 0
        self.use_memory = 0
    
    def _memory_size(self, key, value):
        return len(str(key).encode("utf-8")) + len(str(value).encode("utf-8"))

    def _evict_lru(self):
        key = self.Link.pop_last()
        if key is None: return

        value = self.Hash.get(key)
        if value is not None:
            self.use_memory -= self._memory_size(key, value)
        self.Hash.remove(key)

    def PUT(self, key: str, value: str):
        old_value = self.Hash.get(key)
        
        if old_value is not None:
            self.use_memory -= self._memory_size(key, old_value)
            self.Link.remove(key)

        new_size = self._memory_size(key, value)
        
        while (
            self.max_memory > 0 and
            self.use_memory + new_size > self.max_memory
        ):  self._evict_lru()

        self.Hash.put(key, value)
        self.Link.touch(key)

        self.use_memory += new_size

    def GET(self, key: str):
        value = self.Hash.get(key)

        if value is not None: self.Link.touch(key)
        print(value)

    def DEL(self, key: str):
        value = self.Hash.get(key)

        if value is not None: 
            self.use_memory -= self._memory_size(key, value)

        self.Hash.remove(key)
        self.Link.remove(key)

    def CONTAINS(self, key: str):
        print(self.Hash.contains(key))

    def KEYS(self):
        print(self.Hash.keys())

    def SIZE(self):
        print(self.Hash.size())

    def CONFIG(self, arg1: str, arg2: str, arg3: str):
        if arg1 != 'SET'       : return
        if arg2 != "maxmemory" : return

        self.max_memory = int(arg3)

        while (
            self.max_memory > 0 and
            self.use_memory > self.max_memory
        ): self._evict_lru()

        print("OK") 
        
    
    def INFO(self, arg1: str):
        if arg1 != "memory": return
        
        print(f"used_memory: {self.use_memory}")
        print(f"max_memory : {self.max_memory}")