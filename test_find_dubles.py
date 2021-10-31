import pytest
from main import symbols, board
from main import generate_board


def value_counter(symbol, board):
    counter = 0
    for value in board.values():
        if value == symbol:
            counter += 1
    return counter


def test_every_symbol_in_the_board_has_a_duble():
    generate_board(symbols)
    for value in board.values():
        assert value_counter(value, board) == 2


def test_one_symbol_doesnt_have_a_duble():
    symbols = 2 * list('!@#$%&<>?{}+')
    symbols.pop()
    symbols.append('a')
    generate_board(symbols)
    assert value_counter('a', board) != 2
