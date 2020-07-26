import random
from collections import Counter


class Board:
    def __init__(self, config: str = ' ' * 9):
        config = config.replace('_', ' ')
        self.config = config

    def get_sq(self, x, y):
        return self.config[(3 - y) * 3 + x - 1]

    def whose_turn(self):
        c = Counter(self.config)
        return 'X' if c['X'] == c['O'] else 'O'

    def take_move(self, player=None):
        if player is None:
            player = self.whose_turn()
        while True:
            move = input('Enter the coordinates: ')
            try:
                x, y = move.strip().split(' ')
                x, y = int(x), int(y)
            except ValueError:
                print('You should enter numbers!')
                continue
            if 1 <= x <= 3 and 1 <= y <= 3:
                pass
            else:
                print('Coordinates should be from 1 to 3!')
                continue
            if board.get_sq(x, y) != ' ':
                print('This cell is occupied! Choose another one!')
                continue
            break
        self.config = self.config[:(3 - y) * 3 + x - 1] + player + self.config[(3 - y) * 3 + x:]

    def make_move(self, difficulty='easy', player=None):
        if player is None:
            player = self.whose_turn()
        print('Making move level "%s"' % difficulty)
        p = random.randrange(9)
        while self.config[p] != ' ':
            p = random.randrange(9)
        self.config = self.config[:p] + player + self.config[p + 1:]

    def print(self):
        print('---------')
        for y_coordinate in [3, 2, 1]:
            print('|', end=' ')
            for x_coordinate in [1, 2, 3]:
                print(self.get_sq(x_coordinate, y_coordinate), end=' ')
            print('|')
        print('---------')

    def get_state(self):
        if all([c != ' ' for c in self.config]):
            return 'Draw'
        for player in 'XO':
            # row win:
            for row in range(3):
                if all([c == player for c in self.config[3 * row: 3 * (row + 1)]]):
                    return '%s wins' % player
            # column win:
            for column in range(3):
                if all([c == player for c in self.config[column:: 3]]):
                    return '%s wins' % player
            # diagonal win:
            if all([c == player for c in self.config[:: 4]]) or \
                    all([c == player for c in self.config[2:7: 2]]):
                return '%s wins' % player
        return 'Game not finished'


board = Board()
board.print()

while board.get_state() == 'Game not finished':
    board.make_move('easy', 'X')
    board.print()
    if board.get_state() != 'Game not finished':
        break
    board.take_move('O')
    board.print()

print(board.get_state())
