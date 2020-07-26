from collections import Counter

class Board:
    def __init__(self, config : str):
        config = config.replace('_', ' ')
        self.config = config

    def get_sq(self, x, y):
        return self.config[(3 - y) * 3 + x - 1]

    def whose_turn(self):
        c = Counter(self.config)
        return 'X' if c['X'] == c['O'] else 'O'

    def take_move(self):
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

        player = self.whose_turn()
        self.config = self.config[:(3 - y) * 3 + x - 1] + player + self.config[(3 - y) * 3 + x:]

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


while True:
    initial_config = input('Enter cells: ')
    if any([c not in 'XO_' for c in initial_config]):
        print('Onlt "X", "O" and "_" are accepted.')
        continue
    if len(initial_config) != 9:
        print('Exactly 9 cells are required')
        continue
    break
        
board = Board(initial_config)

board.print()

initial_board_state = board.get_state()

if initial_board_state != 'Game not finished':
    print(initial_board_state)
    exit()

board.take_move()
board.print()
print(board.get_state())