from HashMap import HashMap

class RedisKeyValue:
    def __init__(self):
        self.bhash = HashMap()
    
    def PUT(self, key: str, value: str):
        self.bhash.put(key, value)

    def GET(self, key: str):
        print(self.bhash.get(key))

    def CONTAINS(self, key: str):
        print(self.bhash.contains(key))