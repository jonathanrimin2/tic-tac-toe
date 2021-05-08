![GitHub](https://img.shields.io/github/license/j-tesla/tic-tac-toe?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/j-tesla/tic-tac-toe?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/j-tesla/tic-tac-toe?style=flat-square)

[![DeepSource](https://deepsource.io/gh/j-tesla/tic-tac-toe.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/j-tesla/tic-tac-toe/?ref=repository-badge)

# Tic-Tac-Toe with AI

---

## Description

A simple implementation of tic-tac-toe: You can play with the AI or with a
friend. If you get bored you can watch two AI's fighting too.

To participate, select the `user` mode. As a player, you can select which
position to mark by entering the column (numbers at bottom) and row (numbers on
the left side). See the [Example section](#Example).

For AI, there is `easy`, `medium`, and `unbeatable` mode.

The `easy` mode simply makes random moves.

The `medium` mode AI makes a move using the following process:

1. If it can win in one move (if it has two in a row), it places a third to get
   three in a row and win.
2. If the opponent can win in one move, it plays the third itself to block the
   opponent to win.
3. Otherwise, it makes a random move.

The `unbeatable` mode AI uses [minmax](https://en.wikipedia.org/wiki/Minimax)
algorithm which makes it unbeatable.

## Example

The example below shows how the program works. The greater-than symbol followed
by space (`>`) represents the user input. Notice that it's not the part of the
input.

```
Enter mode for Player 1: > user
Enter mode for Player 2: > medium
  ---------
3 |       |
2 |       |
1 |       |
  ---------
    1 2 3
Enter the coordinates: > 2 2
  ---------
3 |       |
2 |   X   |
1 |       |
  ---------
    1 2 3
Making move level "medium"
  ---------
3 |       |
2 |   X   |
1 | O     |
  ---------
    1 2 3
Enter the coordinates: > 1 3
  ---------
3 | X     |
2 |   X   |
1 | O     |
  ---------
    1 2 3
Making move level "medium"
  ---------
3 | X     |
2 |   X   |
1 | O   O |
  ---------
    1 2 3
Enter the coordinates: > 2 1
  ---------
3 | X     |
2 |   X   |
1 | O X O |
  ---------
    1 2 3
Making move level "medium"
  ---------
3 | X O   |
2 |   X   |
1 | O X O |
  ---------
    1 2 3
Enter the coordinates: > 1 2
  ---------
3 | X O   |
2 | X X   |
1 | O X O |
  ---------
    1 2 3
Making move level "medium"
  ---------
3 | X O   |
2 | X X O |
1 | O X O |
  ---------
    1 2 3
Enter the coordinates: > 3 3
  ---------
3 | X O X |
2 | X X O |
1 | O X O |
  ---------
    1 2 3
Draw

Enter mode for Player 1: > medium
Enter mode for Player 2: > user
  ---------
3 |       |
2 |       |
1 |       |
  ---------
    1 2 3
Making move level "medium"
  ---------
3 |       |
2 |       |
1 |   X   |
  ---------
    1 2 3
Enter the coordinates: > 2 2
  ---------
3 |       |
2 |   O   |
1 |   X   |
  ---------
    1 2 3
Making move level "medium"
  ---------
3 |       |
2 |   O   |
1 | X X   |
  ---------
    1 2 3
Enter the coordinates: > 3 1
  ---------
3 |       |
2 |   O   |
1 | X X O |
  ---------
    1 2 3
Making move level "medium"
  ---------
3 | X     |
2 |   O   |
1 | X X O |
  ---------
    1 2 3
Enter the coordinates: > 1 2
  ---------
3 | X     |
2 | O O   |
1 | X X O |
  ---------
    1 2 3
Making move level "medium"
  ---------
3 | X     |
2 | O O X |
1 | X X O |
  ---------
    1 2 3
Enter the coordinates: > 3 3
  ---------
3 | X   O |
2 | O O X |
1 | X X O |
  ---------
    1 2 3
Making move level "medium"
  ---------
3 | X X O |
2 | O O X |
1 | X X O |
  ---------
    1 2 3
Draw

Enter mode for Player 1: > exit
```

## License

This project is licensed under the MIT License. For details, check the
[LICENSE file](LICENSE).
