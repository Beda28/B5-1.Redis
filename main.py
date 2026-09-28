from service import RedisKeyValue

def execute(command, count, func):
    if len(command) != count:
        print(
            f"(error) ERR wrong number of arguments "
            f"for '{command[0].lower()}' command"
        )
        return
    func(*command[1:])

def main():
    redis = RedisKeyValue()

    while True:
        try: 
            value      = input("mini-redis> ")
            command    = value.split()
            if not command: continue

            raw_command = command[0]
            command[0]  = command[0].upper()

            if   command[0] in ("EXIT", "QUIT"): break

            if   command[0] == "SET"    : execute(command, 3, redis.PUT)
            elif command[0] == "GET"    : execute(command, 2, redis.GET)
            elif command[0] == "DEL"    : execute(command, 2, redis.DEL)
            elif command[0] == "EXISTS" : execute(command, 2, redis.CONTAINS)
            elif command[0] == "DBSIZE" : execute(command, 1, redis.SIZE)
            elif command[0] == "KEYS"   : execute(command, 1, redis.KEYS)

            elif command[0] == "CONFIG" : execute(command, 4, redis.CONFIG)
            elif command[0] == "INFO"   : execute(command, 2, redis.INFO)

            elif command[0] == "EXPIRE" : execute(command, 3, redis.EXPIRE)
            elif command[0] == "TTL"    : execute(command, 2, redis.TTL)

            else: print(f"(error) ERR unknown command '{raw_command}'")

        except IndexError: print("(error) ERR value is not an integer or out of range")
            
if __name__ == "__main__":
    main()