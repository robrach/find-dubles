import random

keys = 'ABCDEFGHIJKLMNOPQRSTUWXY'
symbols = 2*list('!@#$%&<>?{}+')
board = {}


def generate_board(symbols):
    for key in keys:
        symbol = random.choice(symbols)
        board[key] = symbol
        symbols.remove(symbol)
    return board


def print_board(board):
    column_counter = 0
    for key, value in board.items():
        print(f'{key}:{value}   ', end="")
        column_counter += 1
        if column_counter == 5:
            print("")
            column_counter = 0


def get_choice():
    first_choice = 9 #int(input('First choice: '))
    second_choice = 8 #int(input('Second input: '))
    print("")
    return first_choice, second_choice


def check_choice(choice):
    pass


def modify_board(verification, board):
    pass


if __name__ == '__main__':
    board = generate_board(symbols)
    print_board(board)
    choice = get_choice()
    verification = check_choice(choice)
    modify_board(verification, board)

    print(symbols)
    print(board)



