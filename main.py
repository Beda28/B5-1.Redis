from service import RedisKeyValue

def main():
    redis = RedisKeyValue()

    while True:
        try: 
            value      = input("mini redis> ")
            command    = value.split()
            command[0] = command[0].upper()

            if   command[0] in ("EXIT", "QUIT"): break

            if   command[0] == "SET"    : redis.PUT(command[1], command[2])
            elif command[0] == "GET"    : redis.GET(command[1])
            elif command[0] == "DEL"    : redis.DEL(command[1])
            elif command[0] == "EXISTS" : redis.CONTAINS(command[1])
            elif command[0] == "DBSIZE" : redis.SIZE()
            elif command[0] == "KEYS"   : redis.KEYS()

            elif command[0] == "CONFIG" : redis.CONFIG(command[1], command[2], command[3])
            elif command[0] == "INFO"   : redis.INFO(command[1])

            elif command[0] == "EXPIRE" : redis.EXPIRE(command[1], command[2])
            elif command[0] == "TTL"    : redis.TTL(command[1])

            else: print("똑바로 가져와")
        except IndexError:
            print("잘못된 입력입니다. 다시 입력해주세요.")
            
if __name__ == "__main__":
    main()