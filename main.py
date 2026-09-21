from service import RedisKeyValue

def main():
    redis = RedisKeyValue()

    while True:
        value   = input("mini redis> ")
        if (value == "exit" or value == 'quit'): break
        command = value.split(" ")

        if   command[0] == "SET"    : redis.PUT(command[1], command[2])
        elif command[0] == "GET"    : redis.GET(command[1])
        elif command[0] == "DEL"    : redis.DEL(command[1])
        elif command[0] == "EXISTS" : redis.CONTAINS(command[1])
        elif command[0] == "DBSIZE" : redis.SIZE()
        elif command[0] == "KEYS"   : redis.KEYS()

        elif command[0] == "CONFIG" : return
        elif command[0] == "INFO"   : return

        elif command[0] == "EXPIRE" : return
        elif command[0] == "TTL"    : return

        else: return print("똑바로 가져와")

if __name__ == "__main__":
    main()