import random
from collections import Counter

player_modes = ['user', 'easy', 'medium', 'unbeatable']

class Board:

    def __init__(self, config: str = ' ' * 9):
        config = config.replace('_', ' ')
        self.config = config
        self.counter = 0

    def get_sq(self, x, y, config):
        return config[(3 - y) * 3 + x - 1]

    def whose_turn(self, config):
        c = Counter(config)
        return 'X' if c['X'] == c['O'] else 'O'

    def make_move(self, difficulty='easy', player=None):
        if player is None:
            player = self.whose_turn(self.config)
        opponent = 'O' if player == 'X' else 'X'
        if difficulty == 'user':
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
                if self.get_sq(x, y, self.config) != ' ':
                    print('This cell is occupied! Choose another one!')
                    continue
                break
            self.config = self.config[:(3 - y) * 3 + x - 1] + player + self.config[(3 - y) * 3 + x:]
        else:
            print('Making move level "%s"' % difficulty)
            if difficulty == 'unbeatable':
                self.config = self.perform_unbeatable_move(player)

            if difficulty == 'medium':
                difficulty = 'easy'
                for c_index, c in enumerate(self.config):
                    if c == ' ' and ('%s wins' % player) == self.get_state(self.config[:c_index] + player + self.config[c_index + 1:]):
                        self.config = self.config[:c_index] + player + self.config[c_index + 1:]
                        difficulty = 'medium'
                        break
                else:
                    for c_index, c in enumerate(self.config):
                        if c == ' ' and ('%s wins' % opponent) == self.get_state(self.config[:c_index] + opponent + self.config[c_index + 1:]):
                            self.config = self.config[:c_index] + player + self.config[c_index + 1:]
                            difficulty = 'medium'
                            break

            if difficulty == 'easy':
                p = random.randrange(9)
                while self.config[p] != ' ':
                    p = random.randrange(9)
                self.config = self.config[:p] + player + self.config[p + 1:]

    def print(self, config):
        print('---------')
        for y_coordinate in [3, 2, 1]:
            print('|', end=' ')
            for x_coordinate in [1, 2, 3]:
                print(self.get_sq(x_coordinate, y_coordinate, config), end=' ')
            print('|')
        print('---------')

    def get_state(self, config=None):
        if config is None:
            config = self.config
        for player in 'XO':
            # row win:
            for row in range(3):
                if all([c == player for c in config[3 * row: 3 * (row + 1)]]):
                    return '%s wins' % player
            # column win:
            for column in range(3):
                if all([c == player for c in config[column:: 3]]):
                    return '%s wins' % player
            # diagonal win:
            if all([c == player for c in config[:: 4]]) or \
                    all([c == player for c in config[2:7: 2]]):
                return '%s wins' % player
        # Moved to after the win check
        # Reason: If the last move decides the victor, it should not be declared as Draw
        if all([c != ' ' for c in config]):
            return 'Draw'
        return 'Game not finished'

    def perform_unbeatable_move(self, player):
        rank = -999999
        unbeatable_config = self.config
        for c_index, c in enumerate(self.config):
            if c == ' ':
                new_rank = self.get_rank(self.config[:c_index] + player + self.config[c_index + 1:], player)
                print("c_index: " + str(c_index) + "  new_rank: " + str(new_rank))
                if new_rank >= rank:
                    rank = new_rank
                    unbeatable_config = (self.config[:c_index] + player + self.config[c_index + 1:])
        print("Decision_made with self.counter: " + str(self.counter))
        return unbeatable_config

    def get_rank(self, config, player, rank=0, configs=None):
        turn = self.whose_turn(config)
        opponent = 'O' if player == 'X' else 'X'
        #self.print(config)
        #print("Generated rank for config: " + str(rank))
        #print("### Player code: " + str(player) + " ###")
        result = self.get_state(config)
        #print("### State reslt: " + str(result) + " ###")
        if ('%s wins' % player) == result:
            rank = 1
        elif ('%s wins' % opponent) == result:
            rank = -1
        elif 'Draw' == result:
            rank = 0
        else:
            for c_index, c in enumerate(config):
                if c == ' ':
                    # rank = int(rank) + int(self.get_rank(config[:c_index] + turn + config[c_index + 1:], player, rank))
                    # new_rank = int(self.get_rank(config[:c_index] + turn + config[c_index + 1:], player))
                    # self.print(config)
                    # print("config: " + str(config) + "   new_rank: " + str(new_rank) + "   rank: " + str(rank))
                    rank = int(rank) + int(self.get_rank(config[:c_index] + turn + config[c_index + 1:], player))
                    # self.counter = self.counter + 1
                    # print("self.counter: " + str(self.counter))
                    # if self.counter > 200:
                    #     print("AAhaa!")
        return rank

    def is_symmetrical(self, config1, config2):
        return 0


def play(player1='easy', player2='easy'):
    board = Board()
    board.print(board.config)

    while board.get_state() == 'Game not finished':
        board.make_move(player1, 'X')
        board.print(board.config)
        if board.get_state() != 'Game not finished':
            break
        board.make_move(player2, 'O')
        board.print(board.config)

    print(board.get_state())


if __name__ == '__main__':
    while True:
        command = input('Input command: ')
        if command == 'exit':
            break
        command = command.split(' ')
        if command[0] != 'start' or len(command) != 3:
            print('Bad parameters!')
            continue
        elif command[1] not in player_modes or command[2] not in player_modes:
            print('Bad parameters!')
            continue

        play(*command[1:])
