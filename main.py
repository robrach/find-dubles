import random

symbols = 'ABCDEFGH'
symbols = list(symbols)

board = {}

# TODO: Fix this function!!! Actually it doesn't work good!= :(
def generate_board(symbols):
    key = 10
    for board_field in range(2*len(symbols)):
        symbol = random.choice(symbols)
        if symbol in board.values():
            if value_counter(symbol, board) < 2:
                pass
            else:
                symbols.remove(symbol)
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
    column_counter = 0
    for key, value in board.items():
        print(f'{key}:{value}   ', end="")
        column_counter += 1
        if column_counter == 4:
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
    print_board(board)

    print('\n')
    print('A:', value_counter('A', board))
    print('B:', value_counter('B', board))
    print('C:', value_counter('C', board))
    print('D:', value_counter('D', board))
    print('E:', value_counter('E', board))
    print('F:', value_counter('F', board))
    print('G:', value_counter('G', board))
    print('H:', value_counter('H', board))


    print(symbols)



