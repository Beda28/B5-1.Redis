from HashMap import HashMap

class RedisKeyValue:
    def __init__(self):
        self.bhash = HashMap()
    
    def SET(key: str, value: str):
        self.bhash.put(key, value)

    def GET(key: str):
        print(self.bhash.get(key))