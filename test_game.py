import unittest.mock as mock
from unittest.mock import patch
from game import *

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

def test_print_board(capfd):
    printBoard(theBoard)
    
    out, err = capfd.readouterr()
    assert out == " | | \n-+-+-\n | | \n-+-+-\n | | \n"
    
def test_game(monkeypatch):
    move = "7"
