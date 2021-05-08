import random
from collections import Counter

player_modes = ["user", "easy", "medium", "unbeatable"]
default_mode = "easy"
INFINITY = 999999


class Board:
    def __init__(self, config: str = " " * 9):
        config = config.replace("_", " ")
        self.config = config

    def get_sq(self, x, y):
        return self.config[(3 - y) * 3 + x - 1]

    def whose_turn(self, config=None):
        if config is None:
            config = self.config
        c = Counter(config)
        return "X" if c["X"] == c["O"] else "O"

    def make_move(self, difficulty="easy", player=None):
        if player is None:
            player = self.whose_turn()
        opponent = "O" if player == "X" else "X"
        if difficulty == "user":
            while True:
                move = input("Enter the coordinates: ")
                try:
                    x, y = move.strip().split(" ")
                    x, y = int(x), int(y)
                except ValueError:
                    print("You should enter numbers!")
                    continue
                if 1 <= x <= 3 and 1 <= y <= 3:
                    pass
                else:
                    print("Coordinates should be from 1 to 3!")
                    continue
                if self.get_sq(x, y) != " ":
                    print("This cell is occupied! Choose another one!")
                    continue
                break
            self.config = (self.config[:(3 - y) * 3 + x - 1] + player +
                           self.config[(3 - y) * 3 + x:])
        else:
            print('Making move level "%s"' % difficulty)
            if difficulty == "unbeatable":
                self.config = self.perform_unbeatable_move(player)

            if difficulty == "medium":
                difficulty = "easy"
                for c_index, c in enumerate(self.config):
                    if c == " " and ("%s wins" % player) == self.get_state(
                            self.config[:c_index] + player +
                            self.config[c_index + 1:]):
                        self.config = (self.config[:c_index] + player +
                                       self.config[c_index + 1:])
                        difficulty = "medium"
                        break
                else:
                    for c_index, c in enumerate(self.config):
                        if c == " " and ("%s wins" %
                                         opponent) == self.get_state(
                                             self.config[:c_index] + opponent +
                                             self.config[c_index + 1:]):
                            self.config = (self.config[:c_index] + player +
                                           self.config[c_index + 1:])
                            difficulty = "medium"
                            break

            if difficulty == "easy":
                p = random.randrange(9)
                while self.config[p] != " ":
                    p = random.randrange(9)
                self.config = self.config[:p] + player + self.config[p + 1:]

    def print(self):
        print("  ---------")
        for y_coordinate in [3, 2, 1]:
            print("%d |" % y_coordinate, end=" ")
            for x_coordinate in [1, 2, 3]:
                print(self.get_sq(x_coordinate, y_coordinate), end=" ")
            print("|")
        print("  ---------")
        print("    1 2 3  ")

    def get_state(self, config=None):
        if config is None:
            config = self.config
        for player in "XO":
            # row win:
            for row in range(3):
                if all([c == player for c in config[3 * row:3 * (row + 1)]]):
                    return "%s wins" % player
            # column win:
            for column in range(3):
                if all([c == player for c in config[column::3]]):
                    return "%s wins" % player
            # diagonal win:
            if all([c == player for c in config[::4]]) or all(
                [c == player for c in config[2:7:2]]):
                return "%s wins" % player
        # Moved to after the win check
        # Reason: If the last move decides the victor, it should not be declared as Draw
        if all([c != " " for c in config]):
            return "Draw"
        return "Game not finished"

    def perform_unbeatable_move(self, player):
        rank = -INFINITY
        unbeatable_config = self.config
        for c_index, c in enumerate(self.config):
            if c == " ":
                new_config = self.config[:c_index] + player + self.config[
                    c_index + 1:]
                new_rank = self.get_rank(new_config, player)
                if new_rank > rank:
                    rank = new_rank
                    unbeatable_config = new_config
        return unbeatable_config

    def get_rank(self, config, player):
        turn = self.whose_turn(config)
        opponent = "O" if player == "X" else "X"
        result = self.get_state(config)

        if ("%s wins" % player) == result:
            return 1
        if ("%s wins" % opponent) == result:
            return -1
        if "Draw" == result:
            return 0
        # Define -infinity for
        rank = -INFINITY if turn == player else INFINITY
        for c_index, c in enumerate(config):
            if c == " ":
                if turn == player:
                    # Maximize for turns made by player
                    rank = max(
                        rank,
                        self.get_rank(
                            config[:c_index] + turn + config[c_index + 1:],
                            player),
                    )
                else:
                    # Minimize for turns made by opponent
                    rank = min(
                        rank,
                        self.get_rank(
                            config[:c_index] + turn + config[c_index + 1:],
                            player),
                    )
        return rank


def play(player1=default_mode, player2=default_mode):
    board = Board()
    board.print()

    while board.get_state() == "Game not finished":
        board.make_move(player1, "X")
        board.print()
        if board.get_state() != "Game not finished":
            break
        board.make_move(player2, "O")
        board.print()

    print(board.get_state())


if __name__ == "__main__":
    player_num = 1
    mode_commands = list()

    while True:
        print("Available modes: " + ", ".join(player_modes))
        command = (input("Enter mode for Player %d [%s]: " %
                         (player_num, default_mode)) or default_mode)

        if command == "exit":
            break

        if command not in player_modes:
            print("Bad parameters!")
            print("Enter one of the following mode: " +
                  ", ".join(player_modes))

            continue

        mode_commands.append(command)

        if player_num == 1:
            player_num += 1

        else:
            play(*mode_commands)
            player_num = 1
            mode_commands = list()
