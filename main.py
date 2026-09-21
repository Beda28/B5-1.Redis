from service import RedisKeyValue

def main():
    redis = RedisKeyValue()

    while True:
        value   = input("mini redis> ")
        if (value == "exit" or value == 'quit'): break
        command = value.split(" ")
        redis   = RedisKeyValue()

        if   command[0] == "SET"    : return
        elif command[0] == "GET"    : return
        elif command[0] == "DEL"    : return
        elif command[0] == "EXISTS" : return
        elif command[0] == "DBSIZE" : return
        elif command[0] == "KEYS"   : return

        elif command[0] == "CONFIG" : return
        elif command[0] == "INFO"   : return

        elif command[0] == "EXPIRE" : return
        elif command[0] == "TTL"    : return

        else: return print("똑바로 가져와")

if __name__ == "__main__":
    main()