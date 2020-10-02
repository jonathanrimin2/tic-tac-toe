# Tic-Tac-Toe with AI

-----

## Description

A simple implementation of tic-tac-toe:
You can play with the AI or with a friend. If you get bored you can watch two AI's fighting too.
Along with the `easy` mode, which simply makes random moves, `medium` mode and `unbeatable` modes are available.

The `medium` mode AI makes a move using the following process:

1. If it can win in one move (if it has two in a row), it places a third to get three in a row and win.
2. If the opponent can win in one move, it plays the third itself to block the opponent to win.
3. Otherwise, it makes a random move.

The `unbeatable` mode AI uses [minmax](https://en.wikipedia.org/wiki/Minimax) algorithm which makes it unbeatable.

## Example

The example below shows how the program works.
The greater-than symbol followed by space (`> `) represents the user input. Notice that it's not the part of the input.

```
Input command: > start user medium
---------
|       |
|       |
|       |
---------
Enter the coordinates: > 2 2
---------
|       |
|   X   |
|       |
---------
Making move level "medium"
---------
|       |
|   X   |
| O     |
---------
Enter the coordinates: > 1 3
---------
| X     |
|   X   |
| O     |
---------
Making move level "medium"
---------
| X     |
|   X   |
| O   O |
---------
Enter the coordinates: > 2 1
---------
| X     |
|   X   |
| O X O |
---------
Making move level "medium"
---------
| X O   |
|   X   |
| O X O |
---------
Enter the coordinates: > 1 2
---------
| X O   |
| X X   |
| O X O |
---------
Making move level "medium"
---------
| X O   |
| X X O |
| O X O |
---------
Enter the coordinates: > 3 3
---------
| X O X |
| X X O |
| O X O |
---------
Draw

Input command: > start medium user
---------
|       |
|       |
|       |
---------
Making move level "medium"
---------
|       |
|       |
|   X   |
---------
Enter the coordinates: > 2 2
---------
|       |
|   O   |
|   X   |
---------
Making move level "medium"
---------
|       |
|   O   |
| X X   |
---------
Enter the coordinates: > 3 1
---------
|       |
|   O   |
| X X O |
---------
Making move level "medium"
---------
| X     |
|   O   |
| X X O |
---------
Enter the coordinates: > 1 2
---------
| X     |
| O O   |
| X X O |
---------
Making move level "medium"
---------
| X     |
| O O X |
| X X O |
---------
Enter the coordinates: > 3 3
---------
| X   O |
| O O X |
| X X O |
---------
Making move level "medium"
---------
| X X O |
| O O X |
| X X O |
---------
Draw

Input command: > exit
```
