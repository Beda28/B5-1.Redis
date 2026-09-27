from HashMap    import HashMap
from LinkedList import LinkedList
from Heap       import Heap

import time

class RedisKeyValue:
    def __init__(self):
        self.Hash = HashMap()
        self.Link = LinkedList()
        self.LRU  = HashMap()

        self.Exp  = HashMap()
        self.Heap = Heap()

        self.max_memory   = 0
        self.use_memory   = 0
        self.evicted_keys = 0
    
    def _memory_size(self, key, value):
        return len(str(key).encode("utf-8")) + len(str(value).encode("utf-8"))

    def _evict_lru(self):
        node = self.Link.pop_last()
        if node is None: return

        key   = node.key
        value = self.Hash.get(key)

        if value is not None:
            self.use_memory -= self._memory_size(key, value)

        self.Hash.remove(key)
        self.LRU.remove(key)
        self.Exp.remove(key)

        self.evicted_keys += 1

    def _delete_key(self, key):
        value = self.Hash.get(key)

        if value is None: return
        
        self.use_memory -= self._memory_size(key, value)

        node = self.LRU.get(key)
        if node is not None: self.Link.remove_node(node)

        self.Hash.remove(key)
        self.LRU.remove(key)
        self.Exp.remove(key)

    def _check_expire(self, key):
        expire_at = self.Exp.get(key)

        if expire_at is None: return False
        if time.time() >= expire_at:
            self._delete_key(key)
            return True

        return False
    
    def _clear_expired(self):
        now = time.time()

        while self.Heap.size() > 0:
            expire_at, key = self.Heap.peek()
            current        = self.Exp.get(key)
            
            if current is None or current != expire_at:
                self.Heap.pop()
                continue

            if expire_at > now: break

            self.Heap.pop()
            self._delete_key(key)

    def PUT(self, key: str, value: str):
        self._clear_expired()
        new_size = self._memory_size(key, value)

        if self.max_memory > 0 and new_size > self.max_memory:
           return print("(error) OOM command not allowed when used_memory > 'maxmemory'")
        
        old_value = self.Hash.get(key)
        node      = self.LRU.get(key)
        
        if old_value is not None:
            self.use_memory -= self._memory_size(key, old_value)
            if node is not None: self.Link.move_to_front(node)
        
        self.Exp.remove(key)

        while (
            self.max_memory > 0 and
            self.use_memory + new_size > self.max_memory
        ):  self._evict_lru()

        self.Hash.put(key, value)

        if node is None:
            node = self.Link.add_first(key)
            self.LRU.put(key, node)

        self.use_memory += new_size
        print("OK")

    def GET(self, key: str):
        if self._check_expire(key): return print("(nil)")
        value = self.Hash.get(key)

        if value is None: return print("(nil)")

        node = self.LRU.get(key)
        self.Link.move_to_front(node)
        print(f'"{value}"')

    def DEL(self, key: str):
        if self._check_expire(key)    : return print("(integer) 0")
        if not self.Hash.contains(key): return print("(integer) 0")

        self._delete_key(key)
        print("(integer) 1")

    def CONTAINS(self, key: str):
        if self._check_expire(key): return print("(integer) 0")
        if self.Hash.contains(key): print("(integer) 1")
        else                      : print("(integer) 0")

    def KEYS(self):
        self._clear_expired()
        print(self.Hash.keys())

    def SIZE(self):
        self._clear_expired()
        print(f"(integer) {self.Hash.size()}")

    def CONFIG(self, arg1: str, arg2: str, arg3: str):
        memory = int(arg3)

        if arg1 != 'SET'       : return
        if arg2 != "maxmemory" : return
        if memory < 0:
            return print("(error) ERR value is not an integer or out of range")

        self._clear_expired()
        self.max_memory = memory

        while (
            self.max_memory > 0 and
            self.use_memory > self.max_memory
        ): self._evict_lru()

        print("OK") 
        
    
    def INFO(self, arg1: str):
        if arg1 != "memory": return

        self._clear_expired()
        
        print(f"used_memory : {self.use_memory}")
        print(f"max_memory  : {self.max_memory}")
        print(f"evicted_keys: {self.evicted_keys}")

    def EXPIRE(self, key: str, seconds: str):
        if self._check_expire(key)    : return print("(integer) 0")
        if not self.Hash.contains(key): return print("(integer) 0")

        seconds = int(seconds)
        if seconds <= 0:
            self._delete_key(key)
            return print("(integer) 1")

        expire_at = time.time() + seconds

        self.Exp.put(key, expire_at)
        self.Heap.push(expire_at, key)
        print("(integer) 1")

    def TTL(self, key: str):
        if self._check_expire(key)    : return print("(integer) -2")
        if not self.Hash.contains(key): return print("(integer) -2")

        expire_at = self.Exp.get(key)
        if expire_at is None: return print("(integer) -1")

        remain = int(expire_at - time.time())
        print(f"(integer) {remain}")