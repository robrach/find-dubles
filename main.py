import random

keys = 'ABCDEFGHIJKLMNOPQRSTUWXY'.lower()
symbols = 2*list('!@#$%&<>?{}+')
board = {}
dubles = int(len(symbols)/2)
found_dubles = 0


def generate_board(symbols):
    for key in keys:
        symbol = random.choice(symbols)
        board[key] = symbol
        symbols.remove(symbol)
    return board


def print_board(board):
    print(f'\nStatus of found dubles: {found_dubles}/{dubles}')
    column_counter = 0
    for key, value in board.items():
        print(f'{key}:{value}   ', end="")
        column_counter += 1
        if column_counter == 5:
            print("")
            column_counter = 0


def example(board):
    first_choice = keys[0].lower()
    first_choice_symbol = board[first_choice]
    for key in board.keys():
        if board[key] == first_choice_symbol and first_choice != key:
            return f'Example: for FIRST CHOICE "{first_choice}" the SECOND CHOICE is "{key}".'


def get_choice():
    print("")
    first_choice = input('FIRST CHOICE: ')
    second_choice = input('SECOND CHOICE: ')
    if first_choice == second_choice:
        print("You can't input the same first and second choice! Input again.")
        get_choice()
    return first_choice.lower(), second_choice.lower()


def check_choice(choice):
    global found_dubles

    if board[choice[0]] == " " and board[choice[1]] == " ":
        print("Both are empty. You already found them earlier.")
    elif board[choice[0]] == board[choice[1]]:
        print("Good!")
        found_dubles += 1
        modify_board(choice)
    else:
        print("Bad choice...")


def modify_board(choice):
    board[choice[0]], board[choice[1]] = " ", " "


if __name__ == '__main__':
    board = generate_board(symbols)

    print('You must find all dubles.')
    print(example(board))

    while found_dubles < dubles:
        print_board(board)
        choice = get_choice()
        check_choice(choice)
    print_board(board)
    print('\nCongratulations! You found all dubles!')
