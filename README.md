# Tic-Tac-Toe with AI

-----

## Description

A simple implementation of tic-tac-toe:
You can play with the AI or with a friend. If you get bored you can watch two AI's fighting too.
Note that only `easy` mode of AI is available for now. 

## Example

The example below shows how the program works.
The greater-than symbol followed by space (`> `) represents the user input. Notice that it's not the part of the input.

```
Input command: > start
Bad parameters!
Input command: > start easy
Bad parameters!
Input command: > start easy easy
---------
|       |
|       |
|       |
---------
Making move level "easy"
---------
|       |
|     X |
|       |
---------
Making move level "easy"
---------
|       |
| O   X |
|       |
---------
Making move level "easy"
---------
|       |
| O   X |
|     X |
---------
Making move level "easy"
---------
|       |
| O   X |
|   O X |
---------
Making move level "easy"
---------
|       |
| O X X |
|   O X |
---------
Making move level "easy"
---------
|     O |
| O X X |
|   O X |
---------
Making move level "easy"
---------
| X   O |
| O X X |
|   O X |
---------
X wins
 
Input command: > start easy user
---------
|       |
|       |
|       |
---------
Making move level "easy"
---------
|       |
|       |
|     X |
---------
Enter the coordinates: > 2 2
---------
|       |
|   O   |
|     X |
---------
Making move level "easy"
---------
|   X   |
|   O   |
|     X |
---------
Enter the coordinates: > 1 1
---------
|   X   |
|   O   |
| O   X |
---------
Making move level "easy"
---------
|   X X |
|   O   |
| O   X |
---------
Enter the coordinates: > 3 2
---------
|   X X |
|   O O |
| O   X |
---------
Making move level "easy"
---------
| X X X |
|   O O |
| O   X |
---------
X wins
 
Input command: > start user user
---------
|       |
|       |
|       |
---------
Enter the coordinates: > 1 1
---------
|       |
|       |
| X     |
---------
Enter the coordinates: > 2 2
---------
|       |
|   O   |
| X     |
---------
Enter the coordinates: > 1 2
---------
|       |
| X O   |
| X     |
---------
Enter the coordinates: > 2 1
---------
|       |
| X O   |
| X O   |
---------
Enter the coordinates: > 1 3
---------
| X     |
| X O   |
| X O   |
---------
X wins
 
Input command: > exit
```