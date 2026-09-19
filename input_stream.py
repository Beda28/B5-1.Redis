def REPL_Input():
    while True:
        value = input("mini redis> ")

        if (value == "exit" or value == 'quit'): break
        print(value)