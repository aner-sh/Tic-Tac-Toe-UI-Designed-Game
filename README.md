# Tic-Tac-Toe Game in Python (Turtle Graphics)

Welcome to the Tic-Tac-Toe game built using Python's `turtle` library! This project lets you play a fun game of Tic-Tac-Toe directly in your Python environment with a graphical interface. The game allows two players to take turns placing their X's and O's on the board.
![image](https://github.com/user-attachments/assets/e19e117e-b652-43c3-947e-6f2bb59c763a)

## Table of Contents
- [Overview](#overview)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Game Rules](#game-rules)
- [Credits](#credits)

---

## Overview

This is a simple implementation of the classic Tic-Tac-Toe game with Python’s `turtle` graphics module. The board is drawn using Turtle graphics, and players take turns by clicking on the grid to place their marks. The game ends when one player wins, or there is a draw.

---

## How It Works

### Key Functions

1. **Board Rendering (`board()`)**
   - Draws the game board with a 3x3 grid using `turtle`'s pen commands.
   - Displays the title "Let's Play Tic-Tac-Toe" at the top.

2. **Drawing X (`draw_x(row, col)`)**
   - Draws the "X" mark at the specified row and column.
   - Updates the game state and increments the move counter.

3. **Drawing O (`draw_o(row, col)`)**
   - Draws the "O" mark at the specified row and column.
   - Updates the game state and increments the move counter.

4. **Winner Check (`check_winner()`)**
   - Verifies whether there is a winner by checking rows, columns, and diagonals for three matching marks (X or O).
   
5. **Turn Management (`play_turn(y, x)`)**
   - Handles player moves based on mouse clicks.
   - Ensures that players alternate between X and O.
   - Checks for a winner or a draw after each move.

6. **Game Flow (`main()`)**
   - Initializes the game by drawing the board and setting up the mouse click event to play the game.

### Game Mechanics

- **Player Turns**: Players alternate turns, starting with X. X will be drawn in red, and O will be drawn in blue.
- **Winning**: The first player to get three of their marks in a row, column, or diagonal wins the game.
- **Draw**: If all spots are filled and no winner is determined, the game will declare a draw.
- **Illegal Moves**: If a player tries to place a mark on an already filled spot, an "Illegal Move" message will be shown.

---

## Installation

To run this project, you need Python installed with the `turtle` module (which comes by default with most Python installations).

### Steps:

1. Download or clone this repository to your local machine: https://github.com/aner-sh/tic-tac-toe
2. Navigate to the project folder and run the script:
```
python tic_tac_toe.py
```
3. A new window will appear showing the Tic-Tac-Toe board. Click on the cells to play the game!

---

## Game Rules

- **Objective**: The goal is to be the first player to get three of your marks in a row, either horizontally, vertically, or diagonally.
- **Turns**: Players alternate placing their marks on the grid. Player X starts the game.
- **Winning**: The first player to align three of their marks wins the game.
- **Draw**: If the grid is full and no one has won, the game ends in a draw.

---

## Credits

This project was built by me, as a fun exercise to practice Python programming and graphics with the `turtle` library.

---

Feel free to fork this repository, make improvements, or report any issues you find!

---

Enjoy playing Tic-Tac-Toe!
