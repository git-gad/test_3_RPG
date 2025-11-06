def validate_input(char):
    while True:
        if char == 'exit' or char == 'start':
            return char
        else:
            char = input('not valid, try again\n')
