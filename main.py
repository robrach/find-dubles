import random

symbols = 'ABCDEFGH'

i = 1
for symbol in range(len(symbols)):
    print(i, random.choice(symbols))
    i += 1

board = {}


def generate_board(symbols):
    key = 1
    for symbol in range(len(symbols)):
        symbol = random.choice(symbols)
        while symbol in board.values():
            symbol = random.choice(symbols)
        board[f'{i}'] = symbol
        key += 1


def print_board(board):
    pass


def get_choice():
    first_choice = int(input('First choice: '))
    second_choice = int(input('Second input: '))
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


