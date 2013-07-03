
import numpy as np

import boards

X = ord('X')
O = ord('O')
EMPTY = ord('E')

def main():
    for n in range(1, 6):
        board = getattr(boards, 'BOARD_%d' % (n,))
        tttb = TicTacToeBoard.from_board(board)
        winner = tttb.find_winner()
        if winner is not None:
            msg = chr(winner)
        elif tttb.is_done():
            msg = 'is done'
        else:
            msg = 'not done'
        print n, msg

class TicTacToeBoard(object):

    def __init__(self, state=None):
        if state is None:
            state = [[EMPTY] * 3] * 3
        if isinstance(state, str):
            state = [[ord(entry) for entry in line]
                     for line in (line.strip() for line in state.split('\n'))
                     if line]
        state = np.asarray(state, dtype=int)
        assert state.shape == (3,3)
        self.check_state(state)
        self.state = state

    @classmethod
    def from_board(cls, board):
        state = [{0:EMPTY, 1:X, 2:O}[i] for i in board]
        return cls(np.array(state).reshape(3,3))

    @staticmethod
    def check_state(state):
        state = np.asarray(state).ravel()
        is_X = state == X
        is_O = state == O
        is_E = state == EMPTY
        if any((~is_X) & (~is_O) & (~is_E)):
            raise ValueError('invalid cell entry in tic tac toe state')

    def is_won(self):
        return self.find_winner() is not None

    def is_done(self):
        return (self.state == EMPTY).any()

    def is_stalemate(self):
        return self.is_done() and not self.is_won()

    def find_winner(self):
        if self.check_winner(X):
            return X
        if self.check_winner(O):
            return O
        return None

    def check_winner(self, player):
        assert player in (X,O)
        return (self.check_winner_rows(player) or
                self.check_winner_cols(player) or
                self.check_winner_diags(player))

    def check_winner_rows(self, player):
        return any(self.check_winner_set(player, row) for row in self.state)

    def check_winner_cols(self, player):
        return any(self.check_winner_set(player, col) for col in self.state.T)

    def check_winner_diags(self, player):
        return any([self.check_winner_set(player, self.state.ravel()[::4]),
                    self.check_winner_set(player, self.state.ravel()[2:7:2])])

    def check_winner_set(self, player, s):
        return (s == player).all()


__name__ == '__main__' and main()
