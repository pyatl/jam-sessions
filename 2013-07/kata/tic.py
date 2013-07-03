#! bin/python
# code kata tic tac toe

def main():
    # Is this pythonic, define main and call it at the bottom?
    kata()
    
def kata():
    print 'playing tic tac toe'
    # Sample boards for Tic Tac Toe kata
    #
    # 0 = empty, 1 = X, 2 = O

    BOARD_1 = [1, 1, 1, 
               2, 2, 0, 
               2, 2, 0]
    BOARD_2 = [1, 2, 1, 
               2, 1, 0, 
               1, 2, 0]
    BOARD_3 = [0, 2, 1, 
               0, 1, 1, 
               0, 2, 1]
    BOARD_4 = [0, 0, 0, 
               0, 0, 0, 
               0, 0, 0]
    BOARD_5 = [1, 2, 2, 
               2, 1, 1, 
               1, 1, 2]

    print
    print 'testing BOARD_1'
    y = test_board(BOARD_1)

    print
    print 'testing BOARD_2'
    y = test_board(BOARD_2)

    print
    print 'testing BOARD_3'
    y = test_board(BOARD_3)

    print
    print 'testing BOARD_4'
    y = test_board(BOARD_4)

    print
    print 'testing BOARD_5'
    y = test_board(BOARD_5)
            
def test_board(board):
    # see if there is a win
    w = test_win(board)
    if w:
        print w
    else:
        # look for possible wins
        no_solution = True
        board_temp = fill_plays(board, 1)
        w = test_win(board_temp)
        if w:
            no_solution = False
            print 'Xs can still win'
        board_temp = fill_plays(board, 2)
        w = test_win(board_temp)
        if w:
            no_solution = False
            print 'Os can still win'
        if no_solution:
            print 'Draw'


def fill_plays(board, i):
    # fill with test moves to look for possible win solutions
    for n,b in enumerate(board):
        if b == 0:
            board[n] = i
    return board
            

def test_win(board):
    # check for win
    for i in range(3):
        # check rows
        if board[0 + i] == board[3+i] and board[3+i] == board[6+i] and \
           board[0 + i] != 0:
            if board[0 + i] == 1:
                return  'X wins on column '+ str( i)
            else:
                return  'O wins on column '+ str( i)
        if board[0 + 3*i] == board[1+i*3] and board[1+i*3] == board[2+i*3] and \
           board[0 + 3*i] != 0:
            if board[0 + 3*i] == 1:
                return  'X wins on row' + str(i)
            else:
                return  'O wins on row' + str(i)
            
    if board[0] == board[4] and board[4] == board[8] and \
       board[4] != 0:
        if board[4] == 1:
            return 'X wins on diagonal'
        else:
            return 'O wins on diagonal'
    if board[2] == board[4] and board[4] == board[6] and \
       board[4] != 0:
        if board[4] == 1:
            return 'X wins on diagonal'
        else:
            return 'O wins on diagonal'
main()
