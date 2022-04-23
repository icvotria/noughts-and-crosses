from game import printBoard

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

def test_print_board(capfd):
    printBoard(theBoard)
    
    out, err = capfd.readouterr()
    assert out == " | | \n-+-+-\n | | \n-+-+-\n | | \n"