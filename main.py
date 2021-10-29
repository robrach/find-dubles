import random

symbols = 'ABCDEFGH'

board = {}


def generate_board(symbols):
    key = 1
    for symbol in range(len(symbols)):
        symbol = random.choice(symbols)
        while symbol in board.values():
            symbol = random.choice(symbols)
        board[f'{key}'] = symbol
        key += 1
        print(board)
    return board


def value_counter(symbol, board):
    counter = 0
    for value in board.values():
        if value == symbol:
            counter += 1
    return counter


def print_board(board):
    pass


def get_choice():
    first_choice = 9 #int(input('First choice: '))
    second_choice = 8 #int(input('Second input: '))
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
    print_board(board)

    board['9'] = 'A'

    print('\n')
    print(board)
    licznik = value_counter('A', board)
    print(licznik)
